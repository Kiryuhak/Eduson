import allure
from requests import Response

def allure_attachment(entity: Response) -> None:
    endpoint = entity.url
    status_code = str(entity.status_code)
    response = entity.text
    string = response.replace("<", "&lt;")
    response = string.replace(">", "&gt;")
    attachment = (
        """
        	<p><strong>Endpoint:</strong> {}</p>
            <p><strong>Status code:</strong>&nbsp;{}</p>
            <p><strong>Response:</strong> {}</p>
        """
    ).format(endpoint, status_code, response)
    allure.attach(attachment, "entity_response", allure.attachment_type.HTML)