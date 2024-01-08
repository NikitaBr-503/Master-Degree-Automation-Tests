from src.utilities.generic_utilities import generate_email_and_password
from src.utilities.request_utilities import RequestUtility


class CustomerHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtility()
        pass

    def create_customer(self, email=None, password=None, expected_sc=201, **kwargs):
        payload = dict()
        if not email:
            di = generate_email_and_password()
            email = di['email']
        if not password:
            password = 'pass1'

        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
        create_user_json = self.requests_utility.post("wp-json/wc/v3/customers",
                                                      payload=payload,
                                                      expected_sc=expected_sc)
        return create_user_json
