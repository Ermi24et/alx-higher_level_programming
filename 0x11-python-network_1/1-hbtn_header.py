#!/usr/bin/python3
"""
a script that takes in a URL, sends a request to the URL and displays the
the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        x_req_id = response.headers.get('X-Request-Id')
    print(x_req_id)
