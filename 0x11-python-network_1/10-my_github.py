#!/usr/bin/python3
"""
a script that takes github credentials and uses github API to display id
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(url, auth=auth)
    print(req.json().get("id"))
