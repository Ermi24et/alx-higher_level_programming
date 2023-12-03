#!/usr/bin/python3
"""
a script that sends a POST request to URL with a given letter
"""

import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    l = {"q": letter}
    res = requests.post("http://0.0.0.0:5000/search_user", data=l)
    try:
        j_res = res.json()
        if j_res == {}:
            print("No result")
        else:
            print("[{}] {}".format(j_res.get("id"), j_res.get("name")))
    except ValueError:
        print("Not a valid JSON")
