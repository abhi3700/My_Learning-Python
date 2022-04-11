import os
from dotenv import load_dotenv

load_dotenv()  #  take environment variables from .env.


# Get RDP Token service information from Environment Variables
base_URL = os.getenv('RDP_BASE_URL')
print(base_URL)
auth_endpoint = base_URL + os.getenv('RDP_AUTH_URL')
print(auth_endpoint)
esg_endpoint = base_URL + os.getenv('RDP_ESG_URL')
print(esg_endpoint)

# Get RDP Credentials information from Environment Variables
username = os.getenv('RDP_USER')
print(username)
password = os.getenv('RDP_PASSWORD')
print(password)
app_key = os.getenv('RDP_APP_KEY')
print(app_key)
