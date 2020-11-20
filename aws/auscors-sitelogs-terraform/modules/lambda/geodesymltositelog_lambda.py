import os
import json
import urllib2
import logging
import boto3
from boto3.session import Session
from ftplib import FTP
from StringIO import StringIO

from GeodesyMLToSiteLog import geodesymltositelog

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    output_bucket_name, gws_url = os.environ['output_bucket_name'], os.environ['gws_url']

    try:
        sns_message = json.loads(event['Records'][0]['Sns']['Message'])

        logger.info('SiteLogReceived event for fourCharacterId {}'.format(
            sns_message['fourCharacterId']))

    except:
        #except KeyError, IndexError, ValueError:
        logger.error('Malformed Event or SNS Message object:\n{}'.format(event))
        raise

    try:
        request_url = '{}/siteLogs/search/findByFourCharacterId?id={}'.format(
            gws_url, sns_message['fourCharacterId'])
        request = urllib2.Request(request_url, headers={'Accept': 'application/xml'})
        xml_string = urllib2.urlopen(request).read()

    except:
        logger.error('Failed to get GeodesyML document for {} from GWS API'.format(
            sns_message['fourCharacterId']))
        raise

    try:
        site_log_filename, site_log_data = geodesymltositelog.parseXML(xml_string)

    except Exception as err:
        # There is currently no error handling in the xml2log module, so expect any exception
        logger.error('Failed to parse XML to site log for {}:\n{}\n{}\n{}'.format(
            sns_message['fourCharacterId'], str(err), repr(err), xml_string))
        raise

    try:
        boto3.client('s3').put_object(
            Bucket=output_bucket_name, Key=site_log_filename, Body=site_log_data)

        logger.info('Site log XML for {} parsed to s3://{}/{}'.format(
            sns_message['fourCharacterId'], output_bucket_name, site_log_filename))

    except:
        logger.error('Failed to output Site Log data to s3://{}/{}'.format(
            output_bucket_name, site_log_filename))
        raise

    ftp_sitelogs = os.environ['ftp_sitelogs']
    if bool(int(ftp_sitelogs)):
        ftp(site_log_filename, site_log_data)
    else:
        logger.info('Not uploading file {} to FTP, option "ftp_sitelogs" is "{}"'.format(site_log_filename, ftp_sitelogs))

def ftp(filename, content):
    ftp_host = os.environ['ftp_host']
    try:
        ftp_username = os.environ['ftp_username']
        ftp_password = lookup_password(os.environ['ftp_password_key'])
        ftp = FTP(ftp_host)
        ftp.login(ftp_username, ftp_password)
        ftp.storlines('STOR {}'.format(filename), StringIO(content))
        ftp.quit()
    except:
        logger.error('Failed to FTP file {} to {}'.format(filename, ftp_host))
        raise

    logger.info('Uploaded file {} to {}'.format(filename, ftp_host))

def lookup_password(key):
    ssm = session(os.environ['parameter_store_role_arn']).client('ssm')
    return ssm.get_parameter(Name=key, WithDecryption=True)['Parameter']['Value']

def session(role_arn):
    sts_client = boto3.client("sts")
    credentials = sts_client.assume_role(RoleArn=role_arn, RoleSessionName="upload-sitelog-to-ftp")['Credentials']
    return Session(aws_access_key_id=credentials['AccessKeyId'],
                    aws_secret_access_key=credentials['SecretAccessKey'],
                    aws_session_token=credentials['SessionToken'])

    # Get XML from SNS message
    #sns_message = json.loads(event['Records'][0]['Sns']['Message'])
    #xml_string = sns_message['siteLogText']

    # Get XML from prod GWS
    #request_url = 'https://gws.geodesy.ga.gov.au/siteLogs/search/findByFourCharacterId?id={}'.format(
    #    sns_message['fourCharacterId'])
    #request = urllib2.Request(request_url, headers={'Accept': 'application/xml'})
    #xml_string = urllib2.urlopen(request).read()

    # Get XML from prod GWS as JSON object
    #request_url = 'https://gws.geodesy.ga.gov.au/siteLogs/search/findByFourCharacterId?id={}'.format(
    #    sns_message['fourCharacterId'])
    #request = urllib2.Request(request_url)
    #response = urllib2.urlopen(request).read()
    #xml_string = json.loads(response)['siteLogText']
