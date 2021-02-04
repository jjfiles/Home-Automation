import requests
from settings import TOKEN as tk
headers = {"Authorization": "Bearer %s" % tk,}
response = requests.post(
    'https://api.lifx.com/v1/lights/group:Office/toggle',
    headers=headers
)