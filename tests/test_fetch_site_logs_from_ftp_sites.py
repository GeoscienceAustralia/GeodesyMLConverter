import pytest
import os

from fetch_site_logs_from_ftp_sites import gws_list_site_logs

def test_get_gws_site_logs():
    os.environ['gws_url'] = 'https://testgeodesy-webservices.geodesy.ga.gov.au'
    assert len(gws_list_site_logs()) > 1000
