import requests
import allure

from config import url
from checkers.checkers import check_status_200, check_status_404


@allure.suite('thecatapi')
@allure.title('Test success code')
def test_code() -> None:
    response = requests.get(url=f'{url}/images/search')
    check_status_200(response)


@allure.suite('thecatapi')
@allure.title('Test 404 code')
def test_code_404() -> None:
    response = requests.get(url=f'{url}/imagessssssss/search')
    check_status_404(response)
