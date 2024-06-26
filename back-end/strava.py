import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import os
from dotenv import load_dotenv

load_dotenv()

ID = os.getenv('CLIENT_ID')
SECRET = os.getenv('CLIENT_SECRET')
REFRESH_T = os.getenv('REFRESH_TOKEN')
ACCESS = os.getenv('ACCESS_TOKEN')

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': ID,
    'client_secret': SECRET,
    'refresh_token': REFRESH_T,
    'access_token': ACCESS,
    'grant_type': "refresh_token",
    'f': 'json'
}

#print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
#print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

#
print(my_dataset)
