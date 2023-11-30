#!/usr/bin/bash
# a script that takes in a URL, and displays the size of the body of the respo
curl -s "$1" | wc -c
