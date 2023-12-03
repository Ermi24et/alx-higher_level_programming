#!/usr/bin/python3
"""
a script that lists msot recent commits on a given github repo
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1],
                                                              sys.argv[2])

    req = requests.get(url)
    req_json = req.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                req_json[i].get("sha"),
                req_json[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
