import requests
from getpass import getpass
import json

username = input("Enter your username: ")
password = getpass("Enter your password: ")
endpoint = "http://localhost:8000/api/auth/"


auth_response = requests.post(endpoint,
                        json={
                            "username": username,
                            "password": password
                        })

if auth_response.status_code == 200:
    print(auth_response.json())
    
    token = auth_response.json()["token"]
    headers = {
        "Authorization": f"Token {token}"
    }

    endpoint = "http://localhost:8000/api/products/"
    #endpoint = "http://localhost:8000/api/products/all/"
    reponse = requests.get(endpoint, headers=headers)
    print(json.dumps(reponse.json(), indent=2))
else:
    print("Invalid credentials.")
