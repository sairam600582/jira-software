# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sairam0.atlassian.net/rest/api/3/issue"
API_TOKEN = "" //USER TOKEN
auth = HTTPBasicAuth("bisaisairam143p@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "project": {
      "key": "FRON"
    },
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "this is own my fault .",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },       
    "issuetype": {
      "name": "Story"
    },

    "summary": "Create it own fault",   
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
