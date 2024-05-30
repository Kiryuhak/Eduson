import requests
import allure

from config import url, url_auth
from checkers.checkers import check_status_200, check_status_401, check_status_is_not_200


@allure.suite("thecatapi")
@allure.title("Test authentication for catapi")
def test_auth_cat(headers: dict) -> None:
    response = requests.get(url=f"{url}/votes", headers=headers)
    check_status_200(response)


@allure.suite("thecatapi")
@allure.title("Missing headers for catapi")
def test_auth_cat_without_header(headers: dict) -> None:
    response = requests.get(url=f"{url}/votes")
    check_status_is_not_200(response)


@allure.suite("theauthapi")
@allure.title("Test authentication for authapi")
def test_auth(headers_auth: dict) -> None:
    response = requests.get(url=f"{url_auth}/api-keys", headers=headers_auth)
    check_status_200(response)


@allure.suite("theauthapi")
@allure.title("Missing headers for authapi")
def test_auth_without_header() -> None:
    response = requests.get(url=f"{url_auth}/api-keys")
    check_status_401(response)
