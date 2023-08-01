import requests
from settings import TOKEN as tk
headers = {"Authorization": "Bearer %s" % tk,}
on = {
    "power": "on"
}
off = {
    "power": "off"
}
response = requests.put(
    'https://api.lifx.com/v1/lights/all/state',
    headers=headers,
    data=off
)
response = requests.put(
    'https://api.lifx.com/v1/lights/label:B-L1/state',
    headers=headers,
    data=on
)