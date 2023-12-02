#!/usr/bin/python3
# a script that sends a request to the URL and displays the body of the respon

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            response = resp.read().decode("utf-8")
            print(response)
    except urllib.error.HTTPError as exp:
        print("Error code:", exp.code)
