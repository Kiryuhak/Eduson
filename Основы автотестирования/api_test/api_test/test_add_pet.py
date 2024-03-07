from .add_pet import *
import requests
import json

OK_CODE = 200
ERROR_CODE = 405
CATEGORY_NAME = "British cats"
TAG_NAME = "Kitten"
PET_STATUS = "available"
PET_NAME = "Chester"
PHOTO = ["https://bigenc.ru/media/2016/10/27/1235157499/4027.jpg"]


def test_can_add_pet():
    # form payload with constant value
    payload = form_data(CATEGORY_NAME, PET_NAME, PHOTO, TAG_NAME, PET_STATUS)
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
    assert response.get(NAME) == PET_NAME
    assert response.get(CATEGORY).get(NAME) == CATEGORY_NAME
    assert len(response.get(TAGS)) == len(payload.get(TAGS))
    if len(response.get(TAGS)) > 0:
        assert response.get(TAGS)[0].get(NAME) == TAG_NAME
    assert len(response.get(PHOTO_URLS)) == len(payload.get(PHOTO_URLS))
    if len(response.get(PHOTO_URLS)) > 0:
        assert response.get(PHOTO_URLS) == PHOTO
    assert response.get(STATUS) == PET_STATUS
