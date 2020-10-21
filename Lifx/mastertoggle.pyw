import requests
from secrets import TOKEN as tk
headers = {"Authorization": "Bearer %s" % tk,}
response = requests.post(
    'https://api.lifx.com/v1/lights/all/toggle',
    headers=headers
)