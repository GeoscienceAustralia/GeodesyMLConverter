import os
import json
import urllib2
import logging
import boto3

import geodesymltositelog

def lambda_handler(event, context):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

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
        request_url = 'https://{}/siteLogs/search/findByFourCharacterId?id={}'.format(
            os.environ['gws_url'], sns_message['fourCharacterId'])
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
