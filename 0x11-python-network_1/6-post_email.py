#!/usr/bin/python3
"""
a script that sends a POST request to the passed URL with the email as paramet
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email_ = sys.argv[2]
    data_dict = {"email": email_}
    res = requests.post(url, data=data_dict).text
    print(res)
