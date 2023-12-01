#!/usr/bin/python3
"""
a script that takes in a URL, sends a request to the URL and displays
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_req_id = response.headers.get('X-Request-Id')
        print(x_req_id)
