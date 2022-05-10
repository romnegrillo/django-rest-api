import requests

endpoint = "http://localhost:8000/api/products/update/14"

reponse = requests.put(endpoint,
                        json={
                            "title": "My Product Title Updated",
                            "content": "My product content",
                            "price": 11
                        })
print(reponse.json())
