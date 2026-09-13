import os

from dotenv import load_dotenv  # Correct function is load_dotenv

# Load the .env file
load_dotenv()

# Now os.environ.get works perfectly
token = os.environ.get("WEBEX_ACCESS_TOKEN")
print(token)  # This should print the token from your .env file
