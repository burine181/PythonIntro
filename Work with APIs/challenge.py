import requests
import json

base_url = "https://swapi.info/api/"
endpoint = "people/5"

# Response object
response = requests.get(base_url + endpoint)
data = response.json()
print(data['name'])