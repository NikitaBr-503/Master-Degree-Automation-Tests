import random

from src.utilities.db_utilities import DBUtility


class CustomersDB(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM coolsite.wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_random_customer_from_db(self, qty=1):
        sql = "SELECT * FROM coolsite.wp_users WHERE user_email LIKE '%test%';"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))