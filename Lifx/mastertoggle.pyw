from secrets import TOKEN as tk
import requests
headers = {"Authorization": "Bearer %s" % tk,}
response = requests.post('https://api.lifx.com/v1/lights/all/toggle', headers=headers)
