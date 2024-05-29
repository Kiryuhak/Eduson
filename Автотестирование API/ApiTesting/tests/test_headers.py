import requests
import allure

from config import url
from checkers.checkers import check_status_200, check_day_of_the_week, check_x_api_key


@allure.suite('thecatapi')
@allure.title('Test header for requests')
def test_headers(headers: dict) -> None:
    response = requests.get(url=f'{url}/images/search', headers=headers)
    check_status_200(response)
    check_day_of_the_week(response)
    check_x_api_key(response)
