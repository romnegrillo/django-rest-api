import requests

endpoint = "http://localhost:8000/api/products/delete/14/"

reponse = requests.delete(endpoint)
print(reponse)
