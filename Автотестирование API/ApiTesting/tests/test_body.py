import requests
import allure

from config import url
from checkers.checkers import check_not_empty, check_status_200, check_schema, check_image_ids


@allure.suite("thecatapi")
@allure.title("Test image ids for several images")
def test_body_image_ids(headers: dict) -> None:
    response = requests.get(url=f"{url}/votes", headers=headers)
    #print(response.json())
    check_status_200(response)
    check_not_empty(response)
    check_image_ids(response)


@allure.suite("thecatapi")
@allure.title("Test json schema for random image")
def test_body_with_schema(headers: dict) -> None:
    response = requests.get(url=f"{url}/votes", headers=headers)
    check_status_200(response)
    check_not_empty(response)
    check_schema('votes', response.json()[7])
