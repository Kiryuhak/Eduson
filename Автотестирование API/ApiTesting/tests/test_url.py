import requests
import allure

from config import url
from checkers.checkers import check_url, check_status_200


@allure.suite("thecatapi")
@allure.title("Test url")
def test_url() -> None:
	url_full = f"{url}/images/search"
	response = requests.get(url=url_full)
	check_status_200(response)
	check_url(response, url_full)