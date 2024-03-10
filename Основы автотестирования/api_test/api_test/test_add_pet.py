from faker.providers import lorem
from .add_pet import *
import requests
import json
import pytest
from faker import Faker

OK_CODE = 200
ERROR_CODE = 405
CATEGORY_NAME = "British cats"
TAG_NAME = "Kitten"
PET_STATUS = "available"
PET_NAME = "Chester"
PHOTO = ["https://bigenc.ru/media/2016/10/27/1235157499/4027.jpg"]
AVG_CHAR = 10
MAX_CHAR = 256
f = Faker()
f.add_provider(lorem)


@pytest.mark.positive
class TestAddPet:
    @pytest.mark.urgent
    @pytest.mark.parametrize(
        "cat_name, pet_name, photo, tag_name, pet_status",
        [
            (CATEGORY_NAME, PET_NAME, PHOTO, TAG_NAME, PET_STATUS),
            ("", PET_NAME, PHOTO, TAG_NAME, PET_STATUS),
            ("", PET_NAME, [], TAG_NAME, PET_STATUS),
            (CATEGORY_NAME, PET_NAME, PHOTO, "", PET_STATUS),
            (CATEGORY_NAME, PET_NAME, PHOTO, TAG_NAME, ""),
            (f.text(max_nb_chars=AVG_CHAR), f.name(), PHOTO,
             f.text(max_nb_chars=AVG_CHAR), f.text(max_nb_chars=AVG_CHAR)),
            (f.text(max_nb_chars=MAX_CHAR), f.name(), PHOTO,
             f.text(max_nb_chars=MAX_CHAR), f.text(max_nb_chars=MAX_CHAR)),
            ("a", "b", PHOTO, "c", "d")
        ]
    )
    def test_can_add_pet(self, cat_name, pet_name, photo, tag_name, pet_status):
        # form payload with constant value
        payload = form_data(cat_name, pet_name, photo, tag_name, pet_status)
        pet = requests.post(
            url=URL,
            headers=headers,
            data=json.dumps(payload)
        )
        # serialize response body text into json structure
        response = json.loads(pet.text)

        assert pet.status_code == OK_CODE

        assert pet.headers.get(CONTENT_TYPE) == APP_JSON

        # check that response body value correspond with request`s value
        assert response.get(ID) > 0
        assert response.get(NAME) == pet_name
        assert response.get(CATEGORY).get(NAME) == cat_name
        assert len(response.get(TAGS)) == len(payload.get(TAGS))
        if len(response.get(TAGS)) > 0:
            assert response.get(TAGS)[0].get(NAME) == tag_name
        assert len(response.get(PHOTO_URLS)) == len(payload.get(PHOTO_URLS))
        if len(response.get(PHOTO_URLS)) > 0:
            assert response.get(PHOTO_URLS) == photo
        assert response.get(STATUS) == pet_status

    def test_cant_add_pet_without_photo(self):
        payload = form_data_no_photo(CATEGORY_NAME, PET_NAME, TAG_NAME, PET_STATUS)
        pet = requests.post(
            url=URL,
            headers=headers,
            data=json.dumps(payload)
        )

        assert pet.status_code == OK_CODE


@pytest.mark.negative
@pytest.mark.flaky
@pytest.mark.xfail(reason="Bug ID-005, should be fixed in release 2.0")
def test_can_add_pet_without_name():
    payload = form_data(CATEGORY_NAME, "", PHOTO, TAG_NAME, PET_STATUS)
    pet = requests.post(
        url=URL,
        headers=headers,
        data=json.dumps(payload)
    )

    assert pet.status_code == ERROR_CODE


@pytest.mark.negative
def test_cant_send_empty_payload():
    pet = requests.post(
        url=URL,
        headers=headers,
    )

    assert pet.status_code == ERROR_CODE
