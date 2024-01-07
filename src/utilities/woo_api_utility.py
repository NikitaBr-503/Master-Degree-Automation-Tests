import os
import logging as logger

from woocommerce import API

from src.configs.hosts import WOO_API_HOSTS
from src.utilities.credentials_utilities import CredentialsUtility


class WooAPIUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOSTS[self.env]
        self.creds = CredentialsUtility.get_wc_api_keys()
        self.wcapi = API(
            url=self.base_url,
            consumer_key=self.creds['wc_key'],
            consumer_secret=self.creds['wc_secret'],
            version='wc/v3'
        )

    def post(self, wc_endpoint, data=None, expected_sc=200):
        rs = self.wcapi.post(wc_endpoint, data=data)

        status_code = rs.status_code
        assert status_code == int(expected_sc), \
            f'Expected status code {expected_sc} but actual {status_code}'
        return rs.json()

    def get(self, wc_endpoint, params=None, expected_sc=200):
        rs = self.wcapi.get(wc_endpoint, params=params)

        status_code = rs.status_code
        assert status_code == int(expected_sc), \
            f'Expected status code {expected_sc} but actual {status_code}'
        return rs.json()

    def put(self, wc_endpoint, params=None, expected_status_code=200):
        rs_api = self.wcapi.put(wc_endpoint, data=params)
        rs_json = rs_api.json()
        assert rs_api.status_code == int(expected_status_code)

        logger.debug(f"PUT API response: {rs_json}")

        return rs_json
