#!/usr/bin/python3
"""
a scripts sends a request to the URL and displays the body of the response
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
