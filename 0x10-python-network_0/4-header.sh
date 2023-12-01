#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL display body
curl -sH "X-School-User-Id: 98" "$1"
