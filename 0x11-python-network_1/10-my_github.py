#!/usr/bin/python3
"""A Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""

import sys
from requests.auth import HTTPBasicAuth
import requests

if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=auth)
    print(r.json().get('id'))
