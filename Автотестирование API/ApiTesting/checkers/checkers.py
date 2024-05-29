import allure
from requests import Response
from datetime import datetime

from data.images import *
from data.validate import *

@allure.step("Check url in response")
def check_url(response: Response, url: str) -> None:
	assert response.url == url, 'Wrong url'

def check_status(response: Response, status_code) -> None:
	assert response.status_code == status_code, f'Bad request code: {response.status_code}'

@allure.step("Check status code 200 (success)")
def check_status_200(response: Response) -> None:
	check_status(response, 200)

@allure.step("Check that status code is not 200")
def check_status_is_not_200(response: Response) -> None:
	assert response.status_code != 200, 'Could not have status 200'

@allure.step("Check status code 201 (success with source creation)")
def check_status_201(response: Response) -> None:
	check_status(response, 201)

@allure.step("Check status code 404 (wrong source requested)")
def check_status_404(response: Response) -> None:
	check_status(response, 404)

@allure.step("Check status code 401 (authentication)")
def check_status_401(response: Response) -> None:
	check_status(response, 401)

@allure.step("Check status code 400 (bad request)")
def check_status_400(response: Response) -> None:
	check_status(response, 400)

@allure.step("Check day of the week in response header")
def check_day_of_the_week(response: Response) -> None:
	assert response.headers['Date'][:2] == datetime.now().ctime()[:2], "Date in header is invalid"

@allure.step("Check x-api-key key in request headers")
def check_x_api_key(response: Response):
	assert 'x-api-key' in response.request.headers.keys(), "Do not have x-api-key in the request header"

@allure.step("Check that response json is not empty")
def check_not_empty(response: Response) -> None:
	#print(response.json())
	length = len(response.json())
	assert length > 0, 'Empty response'

@allure.step("Check length of the response json")
def check_response_length(response: Response, len_my: int) -> None:
	#print(response.json())
	length = len(response.json())
	assert length == len_my, 'Wrong length of the response'

@allure.step("Check image ids from the body")
def check_image_ids(response: Response) -> None:
	for key, value in image_ids.items():
		assert response.json()[key]['image_id'] == value, f"Invalid id for {key} image"

@allure.step("Check dates order")
def check_dates_order(response: Response) -> None:
	dates = list(map(lambda x: datetime.strptime(x["created_at"], '%Y-%m-%dT%H:%M:%S.000Z'), response.json()))
	for i in range(len(dates)-1):
		assert dates[i] >= dates[i+1]

@allure.step("Check schema by her name")
def check_schema(name: str, json: dict) -> None:
	is_valid = validate_json(name, json)
	assert is_valid == True, 'Given JSON data is InValid'

@allure.step("Check success status")
def check_success(response: Response) -> None:
	assert response.json()['message'] == 'SUCCESS', 'Request was not successed'

@allure.step("Check duplicated favourites")
def check_duplicated(response: Response) -> None:
	assert 'DUPLICATE_FAVOURITE' in response.text, 'Validation for duplicated favourites is broken'
