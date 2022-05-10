import requests
import json

endpoint = "http://localhost:8000/api/products/"
#endpoint = "http://localhost:8000/api/products/all/"

reponse = requests.get(endpoint)
print(json.dumps(reponse.json(), indent=2))
