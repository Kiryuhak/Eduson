import requests
import allure
import string
from random import randrange, choice

from config import url
from helpers.attach import allure_attachment
from helpers.generate_id import generate
from checkers.checkers import check_not_empty, check_status_200, check_schema

class Favourites:
    
    def __init__(self, headers):
        self.headers=headers

    @allure.step("Get favourites") 
    def get_favourites(self, params: dict) -> int:
        params_str = '?'
        for key, value in params.items():
            params_str += key + "=" + str(value) + "&"           
        response = requests.get(url=f"{url}/favourites{params_str}",	
    	                        headers=self.headers)
        check_status_200(response)
        check_not_empty(response)
        return response.json()      
        
    @allure.step("Create favourite") 
    def create_favourite(self) -> int:
        response = requests.post(url=f"{url}/favourites",	
    	                        headers=self.headers,
    							json={
    	  "image_id": generate(),
    	  "sub_id": "my-user-1234"
    	})
        allure_attachment(response)
        check_status_200(response)
        check_not_empty(response)
        check_schema('create', response.json())
        assert response.json()['message'] == 'SUCCESS', 'Favourite was not created'
        return response.json()['id']
    
    @allure.step("Delete favourite") 
    def delete_favourite(self, id: int) -> int:
        response = requests.delete(url=f"{url}/favourites/{id}",	
                                headers=self.headers)
        allure_attachment(response)									
        check_status_200(response)
        check_not_empty(response)
        check_schema('delete', response.json())
        assert response.json()['message'] == 'SUCCESS', 'Favourite was not deleted'
