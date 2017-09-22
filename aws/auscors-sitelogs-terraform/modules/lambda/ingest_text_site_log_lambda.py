import boto3
import json
import logging
import credstash
import os
import requests
import tempfile

from SiteLogToGeodesyML import sitelogtogeodesyml

def lambda_handler(event, context):
    """
    Receive a text site log file from an S3:Put event, convert it to GeodesyML, and upload it to GWS.
    """

    text_site_log_file_name = None
    xml_site_log_file = None
    try:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        s3_event = event['Records'][0]['s3']
        key = s3_event['object']['key']

        logger.info('Received {}'.format(key))

        bucket = s3_event['bucket']['name']
        version_id = s3_event['object']['versionId']

        credstash_role_arn = os.environ['credstash_role_arn']
        gws_url = os.environ['gws_url']
        oauth2_url = os.environ['oauth2_url']

        session_params = credstash.get_assumerole_credentials(credstash_role_arn)
        dynamodb = credstash.get_session(**session_params).resource('dynamodb')

        gws_oidc_client_id = credstash.getSecret(os.environ['gws_oidc_client_id_key'],
                                                 dynamodb=dynamodb)

        gws_oidc_client_password = credstash.getSecret(os.environ['gws_oidc_client_password_key'],
                                                       dynamodb=dynamodb)

        gws_system_user = credstash.getSecret(os.environ['gws_system_user_key'], dynamodb=dynamodb)

        gws_system_user_password = credstash.getSecret(os.environ['gws_system_user_password_key'],
                                                       dynamodb=dynamodb)

        response = requests.post(oauth2_url + '/access_token?realm=/',
                                 auth=(gws_oidc_client_id, gws_oidc_client_password),
                                 data={'grant_type': 'password',
                                       'username': gws_system_user,
                                       'password': gws_system_user_password,
                                       'scope': 'openid profile'})

        response.raise_for_status()
        token = json.loads(response.content)['id_token']

        obj = boto3.resource('s3').Object(bucket, key)
        text_site_log = obj.get(VersionId=version_id)['Body'].read()

        text_site_log_file_name = os.path.join(tempfile.gettempdir(), key)

        with open(text_site_log_file_name, 'w+b') as text_site_log_file:
            text_site_log_file.write(text_site_log)

        xml_site_log_file = tempfile.NamedTemporaryFile(delete=False)

        sitelogtogeodesyml.convert(text_site_log_file_name, xml_site_log_file.name)
        with open(xml_site_log_file.name, 'r+b') as xml_site_log_file:
            xml_site_log = xml_site_log_file.read()

        logger.info('Converted {} to xml: {}'.format(key, xml_site_log))

        headers = {'content-type': 'application/xml', 'Authorization':'Bearer ' + token}
        response = requests.post(gws_url + '/siteLogs/upload', data=xml_site_log, headers=headers)

        response.raise_for_status()

        logger.info('Uploaded generated xml to {}'.format(gws_url))
    except Exception as err:
        if text_site_log_file_name and os.path.exists(text_site_log_file_name):
            os.remove(text_site_log_file_name)

        if xml_site_log_file and os.path.exists(xml_site_log_file.name):
            os.remove(xml_site_log_file.name)

        raise
