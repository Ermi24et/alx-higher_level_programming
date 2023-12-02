#!/usr/bin/python3
"""
a script that fetches a URL
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url).text

    print("Body response:")
    print("\t- type:", type(resp))
    print("\t- content:", resp)
