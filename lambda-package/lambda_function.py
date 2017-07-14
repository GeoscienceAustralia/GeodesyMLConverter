import os
import json
import urllib2
import logging
import boto3

import xml2log

logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    logger = logging.getLogger(__name__)

    try:
        sns_message = json.loads(event['Records'][0]['Sns']['Message'])
        xml_string = sns_message['siteLogText']

        logger.info('SiteLogReceived event for fourCharacterId {}'.format(
            sns_message['fourCharacterId']))

    #except KeyError, IndexError, ValueError:
    except:
        logger.error('Malformed Event or SNS Message object:\n{}'.format(event))
        raise

    try:
        site_log_filename, site_log_data = xml2log.parseXML(xml_string)

    except:
        # There is currently no error handling in the xml2log module, so expect any exception
        logger.error('Failed to parse XML to site log for {}:\n{}'.format(
            sns_message['fourCharacterId'], xml_string))
        raise

    try:
        output_bucket_name = os.environ['output_bucket_name']
        boto3.client('s3').put_object(
            Bucket=output_bucket_name, Key=site_log_filename, Body=site_log_data)

        logger.info('Site log XML for {} parsed to s3://{}/{}'.format(
            sns_message['fourCharacterId'], output_bucket_name, site_log_filename)

    except KeyError:
        logger.error('Output bucket name not given as Lambda environment variable')
        raise

    except:
        logger.error('Failed to output Site Log data to s3://{}/{}'.format(
            output_bucket_name, site_log_filename)
        raise


    # Get XML from GWS
    #request_url = 'https://gws.geodesy.ga.gov.au/siteLogs/search/findByFourCharacterId?id={}'.format(
    #    sns_message['fourCharacterId'])
    #request = urllib2.Request(request_url, headers={'Accept': 'application/xml'})
    #xml_string = urllib2.urlopen(request).read()

