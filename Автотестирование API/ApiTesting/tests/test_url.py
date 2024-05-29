import requests
import allure

from config import url
from checkers.checkers import check_status_200, check_url


@allure.suite('thecatapi')
@allure.title('Test URL')
def test_url() -> None:
    url_full = f'{url}/images/search'
    response = requests.get(url=url_full)
    check_status_200(response)
    check_url(response, url_full)
