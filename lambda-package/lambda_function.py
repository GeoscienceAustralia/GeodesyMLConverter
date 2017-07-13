import os
import json
import urllib2
import logging
import boto3

import xml2log

logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    logger = logging.getLogger(__name__)

    sns_message = json.loads(event['Records'][0]['Sns']['Message'])
    xml_string = sns_message['siteLogText']

    logger.info('SiteLogReceived event for fourCharacterId {}'.format(
        sns_message['fourCharacterId']))

    site_log_filename, site_log_data = xml2log.parseXML(xml_string)

    output_bucket_name = os.environ['output_bucket_name']
    boto3.client('s3').put_object(
        Bucket=output_bucket_name, Key=site_log_filename, Body=site_log_data)

    logger.info('Site log XML for {} parsed to s3://{}/{}'.format(
        sns_message['fourCharacterId'], output_bucket_name, site_log_filename)



    #request_url = 'https://gws.geodesy.ga.gov.au/siteLogs/search/findByFourCharacterId?id={}'.format(
    #    sns_message['fourCharacterId'])
    #request = urllib2.Request(request_url, headers={'Accept': 'application/xml'})
    #xml_string = urllib2.urlopen(request).read()

