# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://sairam0.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF05Vb2f4pXdlrajHwn4EaqcEdjEsN90VO0BY17bnVI05aqaQ0JiiFnAvB2zxD5EmrIF-Y0E3qp8MgS_b-yMyQkqcxFq40VhvzNf3koCsuOGbe_zcwt1l6L6m0U1IkbVvwQ0FH3iak6gQYQtiiSrgehrypR19ClH3SY6qCEUEi4Oyg=C38E2AE1"

    auth = HTTPBasicAuth("bisaisairam143p@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "FRON"
        },
        "issuetype": {
            "name": "Story"
        },
        "summary": "Main order flow broken",
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
