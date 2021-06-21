import sys
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/greenlight/v3"
headers = {
  'FILES-TO-SCAN': '/home/sql/NodeGoat/app/routes/contributions.js',
  'PROJECT-URI': 'https://github.com/accvcar/NodeGoat',
  "User-Agent": "Python HMAC Example"
}
#'PROJECT-NAME': 'NodeGoat-Azure',
if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/scan/js", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Whoops!")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
#        for app in data["_embedded"]["applications"]:
        for app in data:
            print(app)
    else:
        #print(response.status_code)
        print(response)