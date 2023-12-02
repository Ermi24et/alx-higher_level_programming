#!/usr/bin/python3
"""
a script that sends a request and displays the variable X-Request_Id in header
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url).headers
    x_req = resp.get("X-Request-Id")
    print(x_req)
