import requests
import allure

from config import url
from helpers.attach import allure_attachment
from checkers.checkers import check_not_empty, check_status_200, check_status_201, check_status_404, check_schema


class Vote:

    def __init__(self, headers):
        self.headers = headers

    @allure.step("Get vote by id")
    def get_vote(self, id: int) -> None:
        response_2 = requests.get(url=f"{url}/votes/{id}",
                                  headers=self.headers)
        allure_attachment(response_2)
        check_status_200(response_2)
        check_not_empty(response_2)
        check_schema('votes', response_2.json())
        assert response_2.json()['id'] == id, 'Incorrect id'

    @allure.step("Get all votes")
    def get_votes(self) -> list:
        response = requests.get(url=f"{url}/votes",
                                headers=self.headers)
        allure_attachment(response)
        check_status_200(response)
        check_not_empty(response)
        return response.json()

    @allure.step("Create vote")
    def create_vote(self) -> int:
        response = requests.post(url=f"{url}/votes",
                                 headers=self.headers,
                                 json={
                                     "image_id": "asf2",
                                     "sub_id": "my-user-1234",
                                     "value": 1
                                 })
        allure_attachment(response)
        check_status_201(response)
        check_not_empty(response)
        check_schema('create', response.json())
        assert response.json()['message'] == 'SUCCESS', 'Vote was not created'
        return response.json()['id']

    @allure.step("Delete vote by id")
    def delete_vote(self, id: int) -> None:
        response_3 = requests.delete(url=f"{url}/votes/{id}",
                                     headers=self.headers)
        allure_attachment(response_3)
        check_status_200(response_3)
        check_not_empty(response_3)
        check_schema('delete', response_3.json())
        assert response_3.json()['message'] == 'SUCCESS', 'Vote was not deleted'

    @allure.step("Trying to get deleted vote by id")
    def get_deleted_vote(self, id: int) -> None:
        response_4 = requests.get(url=f"{url}/votes/{id}",
                                  headers=self.headers)
        allure_attachment(response_4)
        check_status_404(response_4)
        # check_not_empty(response_4)
        # check_schema('not_found', response_4.json())
        # assert response_4.json()['message'] == 'NOT_FOUND', 'Vote was not deleted'
        assert response_4.text == 'NOT_FOUND', 'Vote was not deleted'
