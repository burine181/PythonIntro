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

for index, character in enumerate(data, start=1):
    print(f"Character #{index}")
    print(f"  Name: {character.get('name')}")
    print(f"  Height: {character.get('height')}")
    print(f"  Mass: {character.get('mass')}")
    print(f"  Gender: {character.get('gender')}")
    print(f"  Birth Year: {character.get('birth_year')}")
    print("-" * 30)