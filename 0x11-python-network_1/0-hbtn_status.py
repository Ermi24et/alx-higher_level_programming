#!/usr/bin/python3
"""
a script that fetches a URL
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        resp = response.read()
    decoded_resp = resp.decode("utf-8")
    print("Body response:")
    print("\t- type:", type(resp))
    print("\t- content:", resp)
    print("\t- utf8 content:", decoded_resp)
