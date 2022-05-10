import requests

endpoint = "http://localhost:8000/api"
reponse = requests.get(endpoint)
print(reponse.json())
