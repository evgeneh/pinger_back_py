import json
import requests 
from requests.adapters import HTTPAdapter

def base_url(route):
    return 'http://localhost:8002{path}'.format(path=route)


headers = {'Content-Type': 'application/json'}

data = {'length':'3', 'data': [{'ip':'192.168.1.1'}, {'ip':'178.154.200.202'},{'ip':'209.185.108.134'}]}
response = requests.post(base_url('/'), data=json.dumps(data), headers=headers)
#print(response.status_code)
print(response.json())


