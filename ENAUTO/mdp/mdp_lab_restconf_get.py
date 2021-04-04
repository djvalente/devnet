
import json
import requests

requests.packages.urllib3.disable_warnings() #pylint: disable=C0322

api_url = "https://192.168.118.134/restconf/data/ietf-interfaces:interfaces"

headers = { "Accept": "application/yang-data+json", 
             "Content-type":"application/yang-data+json"
           }

basicauth = ("cisco", "Cisco123!")

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

response_json = resp.json()

print(json.dumps(response_json, indent=4))