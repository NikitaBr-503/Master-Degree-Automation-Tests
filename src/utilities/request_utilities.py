import os

import requests
import json
import logging as logger
from requests_oauthlib import OAuth1

from src.configs.hosts import API_HOSTS
from src.utilities.credentials_utilities import CredentialsUtility


class RequestUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.creds = CredentialsUtility.get_wc_api_keys()
        self.auth = OAuth1(client_key=self.creds['wc_key'],
                           client_secret=self.creds['wc_secret'])

    def post(self, endpoint, payload=None, headers=None, expected_sc=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.post(url=url,
                               data=json.dumps(payload),
                               headers=headers,
                               auth=self.auth)
        status_code = rs_api.status_code
        assert status_code == int(expected_sc), \
            f'Expected status code {expected_sc} but actual {status_code}'
        logger.debug(f'API POST response: {rs_api.json()}')
        return rs_api.json()

    def get(self, endpoint, payload=None, headers=None, expected_sc=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.get(url=url,
                              data=json.dumps(payload),
                              headers=headers,
                              auth=self.auth)

        status_code = rs_api.status_code
        assert status_code == int(expected_sc), \
            f'Expected status code {expected_sc} but actual {status_code}'
        logger.debug(f'API GET response: {rs_api.json()}')
        return rs_api.json()
