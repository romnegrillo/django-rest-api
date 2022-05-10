import requests

endpoint = "http://localhost:8000/api/products/"

reponse = requests.post(endpoint,
                        json={
                            "title": "My Product Title",
                            "content": "My product content",
                            "price": 123.45
                        })
print(reponse.json())
