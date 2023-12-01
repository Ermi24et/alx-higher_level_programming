#!/bin/bash
# sends a GET response to a given URL and displays the response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
