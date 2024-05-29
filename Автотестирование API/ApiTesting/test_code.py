import requests
import allure

from config import url
from checkers.checkers import check_status_200, check_status_404, check_url


@allure.suite('thecatapi')
@allure.title('Test success code')
def test_code() -> None:
    response = requests.get(url=f'{url}/images/search')
    check_status_200(response)


@allure.suite('thecatapi')
@allure.title('Test URL')
def test_url() -> None:
    url_full = f'{url}/images/search'
    response = requests.get(url=url_full)
    check_status_200(response)
    check_url(response, url_full)


@allure.suite('thecatapi')
@allure.title('Test 404 code')
def test_code_404() -> None:
    response = requests.get(url=f'{url}/imagessss/search')
    check_status_404(response)
