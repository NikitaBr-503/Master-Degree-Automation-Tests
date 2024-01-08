from src.utilities.generic_utilities import generate_random_string
from src.utilities.request_utilities import RequestUtility


class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f'wp-json/wc/v3/products/{product_id}')

    def create_product(self, payload=None):
        if not payload:
            payload = {
                'name': generate_random_string(),
                'type': 'simple',
                'regular_price': '10.99',
            }

        rs_api = self.requests_utility.post('wp-json/wc/v3/products',
                                            payload=payload,
                                            expected_sc=201)
        return rs_api

    def call_list_products(self, payload=None):
        return self.requests_utility.get('wp-json/wc/v3/products', payload=payload)