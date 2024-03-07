URL = "https://petstore.swagger.io/v2/pet"
CONTENT_TYPE = "Content-Type"
APP_JSON = "application/json"
ID = "id"
NAME = "name"
CATEGORY = "category"
TAGS = "tags"
PHOTO_URLS = "photoUrls"
STATUS = "status"

headers = {
    CONTENT_TYPE: APP_JSON
}

# form full request body with parameters
def form_data(category_name, pet_name, photo, tag_name, status):
    return {
        ID: 1,
        CATEGORY: {
            ID: 1,
            NAME: category_name
        },
        NAME: pet_name,
        PHOTO_URLS: photo,
        TAGS: [
            {
                ID: 1,
                NAME: tag_name
            }
        ],
        STATUS: status
    }

# form request body without photo
def form_data_no_photo(category_name, pet_name, tag_name, status):
    return {
        ID: 1,
        CATEGORY: {
            ID: 1,
            NAME: category_name
        },
        NAME: pet_name,
        TAGS: [
            {
                ID: 1,
                NAME: tag_name
            }
        ],
        STATUS: status
    }
