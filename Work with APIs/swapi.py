import requests
import json

base_url = "https://swapi.info/api/"
endpoint = "people/"

# Response object
response = requests.get(base_url + endpoint)
# print(response)
# print("Text:")
# print(response.text)
# print("Status Code:")
# print(response.status_code)
# print("Headers:")
# print(response.headers)
data = response.json()
print(data[0]['name'])  # Print the name of the first character

