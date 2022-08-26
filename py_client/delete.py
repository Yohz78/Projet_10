import requests

project_id = input("quel id ?")
try:
    project_id = int(project_id)
    print(f"{project_id}")
except:
    project_id = None
    print(f"{project_id} is not valid")

if project_id:
    endpoint = f"http://localhost:8000/api/projects/{project_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)
