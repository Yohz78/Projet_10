import requests

# endpoint = "https://www.httpbin.org/status/200"
# endpoint = "https://www.httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(
    endpoint, json={"title": "camarche?", "description": "Oups"}
)
print(get_response.json())
# print(get_response.status_code)
