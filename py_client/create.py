import requests

endpoint = "http://localhost:8000/api/products/create/"

data = {
    "title": "Title of the product",
    "price": 31.50
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
