import requests

endpoint = "http://localhost:8000/api/"
reponse = requests.get(endpoint,
                       params={"param1": "value1", "param2": "value2"},
                       json={"query": "hello"})
print(reponse.text)
