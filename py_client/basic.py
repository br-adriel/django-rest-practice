import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"query": "Hello world"})
print(get_response.json()['message'])
print(get_response.status_code)
