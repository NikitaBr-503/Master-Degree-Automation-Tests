import pytest

from src.helpers.apiHelpers.products_helper import ProductsHelper
from src.helpers.dbHelper.products_db import ProductsDB
from src.utilities.request_utilities import RequestUtility

pytest_mark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestUtility()
    rs_api = req_helper.get(endpoint='wp-json/wc/v3/products')
    assert rs_api


@pytest.mark.tcid25
def test_get_product_by_id():
    product_db = ProductsDB().get_random_product_from_db(1)
    product_id = product_db[0]['ID']
    db_name = product_db[0]['post_title']

    rs_api = ProductsHelper().get_product_by_id(product_id)
    api_name = rs_api['name']

    assert db_name == api_name