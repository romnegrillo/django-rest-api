import requests

endpoint = "http://localhost:8000/api/products/7"

reponse = requests.get(endpoint)
print(reponse.json())
