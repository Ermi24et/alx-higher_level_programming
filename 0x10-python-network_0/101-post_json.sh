
#!/bin/bash
# sends a JSON POST request to a given URL with a given JSON file.
cat "$2" | curl -sX POST -H "Content-Type: application/json" -d @- "$1"
