from datetime import datetime, timedelta

import pytest

from src.helpers.apiHelpers.products_helper import ProductsHelper
from src.helpers.dbHelper.products_db import ProductsDB


@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
        days_from_today = 30
        after_date = datetime.now().replace(microsecond=0) - timedelta(days=days_from_today)
        after_date = after_date.isoformat()
        payload = {'after': after_date}

        rs_api = ProductsHelper().call_list_products(payload=payload)
        rs_db = ProductsDB().get_products_created_after_given_date(date=after_date)
        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in rs_db]
        ids_diff = list(set(ids_in_api) - set(ids_in_db))

        # assert ids_in_api == ids_in_db
        assert rs_api
        assert len(rs_api) == len(rs_db)
        assert not ids_diff
