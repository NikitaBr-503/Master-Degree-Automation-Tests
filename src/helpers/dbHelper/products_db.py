import random

from src.utilities.db_utilities import DBUtility


class ProductsDB(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        sql = "SELECT * FROM coolsite.wp_posts WHERE post_type = 'product' LIMIT 100;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):
        sql = f"SELECT * FROM coolsite.wp_posts WHERE ID = {product_id};"

        return self.db_helper.execute_select(sql)

    def get_products_created_after_given_date(self, date):
        sql = f'SELECT * FROM coolsite.wp_posts WHERE post_type = "product" AND post_date > "{date}" LIMIT 100;'
        return self.db_helper.execute_select(sql)
