import pytest
import allure

from config import key, key_auth


#header for authentication, not working for some methods
@allure.step('Add headers for catapi')
@pytest.fixture(scope='session')
def headers() -> dict:
    return {'x-api-key': key}


#header for authentication
@allure.step('Add headers for authapi')
@pytest.fixture(scope='session')
def headers_auth() -> dict:
    return {'x-api-key': key_auth}
    #return {'apiKey': key_auth}
