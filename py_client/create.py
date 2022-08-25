import requests


endpoint = "http://localhost:8000/api/projects/"

data = {
    "title": "camarche?",
    "description": "Oups",
    "type": "test",
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())
