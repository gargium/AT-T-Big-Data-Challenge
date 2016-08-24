import requests
from requests.auth import HTTPBasicAuth

apikey = "3f86af875f65b032c0bbba0f01eb1d31e8e2f756"
request_url = "http://citysdk.commerce.gov"

request_obj = {
  'level': 'county',
  'sublevel': True,
  'lat': '37.7799',
  'lng': '-121.9780',
  'api': 'acs5',
  'year': 2011,
  'variables': ['income', 'median_home_value']
}

response = requests.post(request_url, auth=HTTPBasicAuth(apikey, None), json=request_obj)

print response.json()
