#!/usr/bin/python3
"""
a script that sends a POST request to the passed URL with the email
"""

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        resp = response.read().decode('utf-8')
        print(resp)
