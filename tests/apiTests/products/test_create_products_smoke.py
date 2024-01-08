import pytest

from src.helpers.apiHelpers.products_helper import ProductsHelper
from src.helpers.dbHelper.products_db import ProductsDB
from src.utilities.generic_utilities import generate_random_string


@pytest.mark.tcid26
def test_create_simple_product():
    payload = {
        'name': generate_random_string(),
        'type': 'simple',
        'regular_price': '10.99',
    }

    product_rs_api = ProductsHelper().create_product(payload)
    product_db = ProductsDB().get_product_by_id(product_rs_api['id'])

    assert product_rs_api
    assert product_rs_api['name'] == payload['name']
    assert payload['name'] == product_db[0]['post_title']