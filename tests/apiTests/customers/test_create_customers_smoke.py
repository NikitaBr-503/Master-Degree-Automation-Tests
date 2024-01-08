import pytest
import logging as logger

from src.helpers.apiHelpers.customer_helper import CustomerHelper
from src.helpers.dbHelper.customers_db import CustomersDB
from src.utilities.generic_utilities import generate_email_and_password


@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_with_password_and_email():
    logger.info('Create a new customer with email and password only')
    credentials = generate_email_and_password()
    email = credentials['email']
    password = credentials['password']

    customer_object = CustomerHelper()
    customer_api_info = customer_object.create_customer(email=email, password=password)

    assert customer_api_info['email'] == email

    cust_db = CustomersDB()
    cust_info = cust_db.get_customer_by_email(email)

    id_in_api = customer_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    cust_db = CustomersDB()
    cust_info = cust_db.get_random_customer_from_db()
    existing_email = cust_info[0]['user_email']

    customer_object = CustomerHelper()
    response_info = customer_object.create_customer(email=existing_email,
                                                    password='fail',
                                                    expected_sc=400)
    assert response_info['code'] == 'registration-error-email-exists'
