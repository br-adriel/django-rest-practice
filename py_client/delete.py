import requests

product_id = int(input("what is the product id? "))
endpoint = f"http://localhost:8000/api/products/{product_id}/delete"

get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code == 204)
