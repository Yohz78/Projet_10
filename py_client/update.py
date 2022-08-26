import requests


endpoint = "http://localhost:8000/api/projects/29/update/"

data = {"title": "Helljlkhkjh", "description": "Test"}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
