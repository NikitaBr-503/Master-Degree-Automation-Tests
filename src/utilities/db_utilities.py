import os

import pymysql
import pymysql.cursors
import logging as logger

from src.configs.hosts import DB_HOST
from src.utilities.credentials_utilities import CredentialsUtility


class DBUtility(object):
    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        self.machine = os.environ.get('MACHINE')
        self.wp_host = os.environ.get('WP_HOST')
        self.env = os.environ.get('ENV', 'test')

        if self.machine == 'docker' and self.wp_host == 'local':
            raise Exception(f"Cannot run test in docker if WP_HOST=local")
        self.host = DB_HOST[self.machine][self.env]['host']
        self.port = DB_HOST[self.machine][self.env]['port']
        self.database = DB_HOST[self.machine][self.env]['database']
        self.table_prefix = DB_HOST[self.machine][self.env]['table_prefix']

    def create_connection(self):
        connection = pymysql.connect(host=self.host,
                                     user=self.creds['db_user'],
                                     password=self.creds['db_password'],
                                     port=self.port)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass
