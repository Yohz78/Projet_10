import requests

headers = {"Authorization": "Bearer adcf3bf223908e5f77b65c1e52f54ebe7b645106"}
endpoint = "http://localhost:8000/api/projects/"

data = {
    "title": "camarche?",
    "description": "Oups",
    "type": "test",
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
