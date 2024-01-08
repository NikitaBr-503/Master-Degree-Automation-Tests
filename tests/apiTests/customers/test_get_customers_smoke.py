import pytest

from src.utilities.request_utilities import RequestUtility


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtility()
    rs_api = req_helper.get('wp-json/wc/v3/customers')
    assert rs_api, f'Response of list all customers is empty'
