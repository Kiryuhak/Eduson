import json
import jsonschema
from jsonschema import validate

def get_schema(name: str) -> dict:
    """This function loads the given schema available"""
    with open(f"data/schemas/{name}.json", 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(name: str, json_data: dict) -> bool:
	"""REF: https://json-schema.org/ """
	# Describe what kind of json you expect.
	execute_api_schema = get_schema(name)	

	message = f"{name} JSON schema is Valid"
	state = True

	try:
		validate(instance=json_data, schema=execute_api_schema)
	except jsonschema.exceptions.ValidationError as err:
		print(err)
		message = f"{name} JSON schema is InValid"
		state = False

	print (message)
	return state
