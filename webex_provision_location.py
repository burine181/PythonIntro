import os
import time
import requests
import json

# ⚠️ SECURITY: Pulling token from Environment Variables to prevent leaks
# ACCESS_TOKEN = os.environ.get("WEBEX_ACCESS_TOKEN", "YOUR_FALLBACK_TOKEN_IF_NEEDED")
from dotenv import load_dotenv  # Correct function is load_dotenv

# Load the .env file
load_dotenv()

# Now os.environ.get works perfectly
ACCESS_TOKEN = os.environ.get("WEBEX_ACCESS_TOKEN")
print(ACCESS_TOKEN)  # This should print the token from your .env file

# ACCESS_TOKEN = "YjI5NmFkOTYtOTNhMy00YTcwLTgwY2MtODRjNjc1ZjhlNGIzMTQyNjM5YTYtOWEx_PF84_e27c5e2a-fb38-4f6d-a6b7-7078240fc441"
BASE_URL = "https://webexapis.com/v1/locations"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def make_request_with_rate_limit(url, headers, max_retries=3):
    """
    Makes an HTTP GET request while handling Webex rate limits (HTTP 429).
    Automatically waits based on the 'Retry-After' header if throttled.
    """
    retries = 0
    while retries < max_retries:
        response = requests.get(url, headers=headers)
        
        # Check if we hit a Rate Limit (HTTP 429)
        if response.status_code == 429:
            # Webex usually provides a 'Retry-After' header indicating how many seconds to wait
            retry_after = int(response.headers.get("Retry-After", 5))
            print(f"Rate limited (429). Pausing for {retry_after} seconds before retrying...")
            time.sleep(retry_after)
            retries += 1
            continue
            
        return response
    
    print("Max retries reached due to persistent rate limiting.")
    return None

# 1. Fetch data from the Webex API using the rate-limited handler
print("Fetching locations from Webex API...")
response = make_request_with_rate_limit(BASE_URL, headers)

# 2. Process data if the request was successful
if response and response.status_code == 200:
    data = response.json()

    print("\n--- Parsing Location Items ---\n")
    for index, item in enumerate(data.get("items", []), start=1):
        print(f"Location #{index}")
        print(f"  Name: {item.get('name')}")
        print(f"  ID: {item.get('id')}")
        
        # Extract nested address fields safely
        address = item.get("address", {})
        # full_address = f"{address.get('address1')}, {address.get('city')}, {address.get('state')} {address.get('postalCode')}"
        # print(f"  Address: {full_address}")
        print(f"  Address: {address.get('address1')}")
        print(f"  City: {address.get('city')}")
        print(f"  State: {address.get('state')}")
        print(f"  Zip Code: {address.get('postalCode')}")
        print(f"  Time Zone: {item.get('timeZone')}")
        
        # Safely handle notes in case they are None/missing
        notes = item.get('notes')
        formatted_notes = notes.replace(chr(10), ' | ') if notes else "No notes"
        print(f"  Notes: {formatted_notes}")
        print("-" * 50)
        
        # Optional: Uncomment the line below if you plan to loop and make 
        # individual secondary API calls per location to avoid hammering the API.
        # time.sleep(0.2) 
        
else:
    status = response.status_code if response else "No Response"
    print(f"Failed to fetch locations. Status Code: {status}")
    if response:
        print(response.text)