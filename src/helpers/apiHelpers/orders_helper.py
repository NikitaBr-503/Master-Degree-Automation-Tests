import json
import os

from src.helpers.dbHelper.orders_db import OrdersDB
from src.utilities.woo_api_utility import WooAPIUtility


class OrdersHelper(object):

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()

    def create_order(self, add_args=None):
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)

        if add_args:
            assert isinstance(add_args, dict)
            payload.update(add_args)

        rs_api = self.woo_helper.post('orders', data=payload, expected_sc=201)
        return rs_api

    @staticmethod
    def verify_order_is_created(order_json, exp_cust_id, exp_products):
        orders_db = OrdersDB()

        # verify response
        assert order_json, f"Create order response is empty."
        assert order_json['customer_id'] == exp_cust_id

        assert len(order_json['line_items']) == len(exp_products)

        # verify db
        order_id = order_json['id']
        line_info = orders_db.get_order_lines_by_order_id(order_id)
        assert line_info

        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        assert len(line_items) == 1

        # get list of product ids in the response
        api_product_ids = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            assert product['product_id'] in api_product_ids

    def call_update_an_order(self, order_id, payload):
        return self.woo_helper.put(f'orders/{order_id}', params=payload)

    def call_retrieve_an_order(self, order_id):
        return self.woo_helper.get(f"orders/{order_id}")