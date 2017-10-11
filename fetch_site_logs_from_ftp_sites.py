"""
Fetch updated site log files from remote FTP sites and upload them to GWS incoming site log bucket.
"""

import logging
import datetime
import ftplib
import os
import re
import shutil
import tempfile

import boto3
import dateutil.parser
import requests

logger = logging.getLogger(__name__) # pylint: disable=invalid-name
logger.setLevel(logging.INFO)

class SiteLogFtpSource(object):
    def __init__(self, host, path):
        self.host = host
        self.path = path

site_log_ftp_sources = [ # pylint: disable=invalid-name
    SiteLogFtpSource('igscb.jpl.nasa.gov', '/pub/station/log'),
    SiteLogFtpSource('161.65.59.67', '/gps/sitelogs/logs'),
]

def parse_date(string):
    """
    Given date in format 'yyyymmdd', return python date(yyyy, mm, dd)
    """
    return datetime.date(int(string[0:4]), int(string[4:6]), int(string[6:8]))

def parse_site_log_file_name(file_name):
    """
    Given site log file name in format 'abcd_yyyymmdd.log', return ('abcd', date(yyyy, mm, dd))
    """
    return file_name[0:4], parse_date(file_name[5:13])

class LogHunter(object):
    site_log_file_name_pattern = re.compile(r'(?P<file_name>\w{4}_\d{8}\.log)', re.IGNORECASE)

    def __init__(self, ftp_sources, current_site_logs):
        self.ftp_sources = ftp_sources
        self.ftp_connections = []
        self.current_site_logs = current_site_logs

        for ftp_source in self.ftp_sources:
            try:
                ftp = ftplib.FTP(ftp_source.host)
                ftp.set_debuglevel(0)
                ftp.login('anonymous', 'anonymous@ga.gov.au')
                ftp.cwd(ftp_source.path)

                self.ftp_connections.append(ftp)
            except Exception as err: #pylint: disable=broad-except
                logger.warn(err, exc_info=True)

    def with_site_log_updates(self, update_handler):
        download_directory_name = tempfile.mkdtemp()

        for _four_char_id, (ftp, remote_file_name) in self.get_site_log_updates().iteritems():
            try:
                downloaded_file_name = self.download(ftp, remote_file_name, download_directory_name)
                logger.info('Downloaded ' + remote_file_name + ' from ' + ftp.host)
                with file(downloaded_file_name, 'rb') as downloaded_file:
                    update_handler(downloaded_file)
            except Exception as err: #pylint: disable=broad-except
                logger.error(err, exc_info=True)

        if not os.listdir(download_directory_name):
            logger.info('No updates found')

        shutil.rmtree(download_directory_name)

    def download(self, ftp, file_name, directory):
        download_path = os.path.join(directory, file_name)
        site_log_file = open(download_path, 'wb')
        ftp.retrbinary('RETR ' + file_name, site_log_file.write)
        site_log_file.close()
        return site_log_file.name

    def get_site_log_updates(self):
        remote_file_names = []

        def collect_remote_file_names(ftp, line):
            match = re.search(type(self).site_log_file_name_pattern, line)
            if match:
                remote_file_names.append((ftp, match.group('file_name')))
            else:
                return None

        for ftp in self.ftp_connections:
            try:
                logger.info('Fetching site log listing from ' + ftp.host)
                ftp.retrlines("LIST", lambda line, ftp=ftp: collect_remote_file_names(ftp, line))
            except Exception as err: #pylint: disable=broad-except
                logger.warn(err, exc_info=True)

        # sort by file name
        remote_file_names.sort(key=lambda remote_file_name: remote_file_name[1])

        remote_site_logs = {}

        for remote_file_name in remote_file_names:
            four_char_id, date_prepared = parse_site_log_file_name(remote_file_name[1])

            if four_char_id in self.current_site_logs:
                if date_prepared > self.current_site_logs[four_char_id]:
                    remote_site_logs[four_char_id] = (remote_file_name[0], remote_file_name[1])

        return remote_site_logs

def gws_list_site_logs():
    site_logs = {}

    gws_url = os.environ['gws_url']
    response = requests.get(gws_url + '/siteLogs?projection=datePrepared&size=10000')
    response.raise_for_status()
    for site_log in response.json()['_embedded']['siteLogs']:
        site_logs[site_log['fourCharacterId'].lower()] = dateutil.parser.parse(site_log['datePrepared']).date()

    return site_logs

def lambda_handler(event, context):
    logHunter = LogHunter(site_log_ftp_sources, gws_list_site_logs())

    s3 = boto3.client('s3')
    incoming_bucket_name = os.environ['incoming_bucket_name']

    def upload_site_log(site_log_file, bucket_name):
        s3.put_object(
            Bucket=bucket_name,
            Key=os.path.split(site_log_file.name)[1],
            Body=site_log_file)

        logger.info('Uploaded ' + os.path.split(site_log_file.name)[1] + ' to s3://' + bucket_name)

    logHunter.with_site_log_updates(lambda site_log_file: upload_site_log(site_log_file, incoming_bucket_name))

if __name__ == '__main__':
    loggerStreamHandler = logging.StreamHandler()
    loggerStreamHandler.setLevel(logging.INFO)
    logger.addHandler(loggerStreamHandler)
    lambda_handler(None, None)
