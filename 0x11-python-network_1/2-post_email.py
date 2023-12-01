#!/usr/bin/python3
"""
a script that sends a POST request to the passed URL with the email as a param
"""

import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

if __name__ == "__main__":
    with urllib.request.urlopen(url, data=data) as response:
        resp = response.read().decode('utf-8')
        print(resp)
