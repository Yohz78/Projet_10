import requests


endpoint = "http://localhost:8000/api/projects/1"

get_response = requests.get(
    endpoint, json={"title": "camarche?", "description": "Oups"}
)
print(get_response.json())
