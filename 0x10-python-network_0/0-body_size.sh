#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the response body size using curl
size=$(curl -s "$1" | wc -c)

# Display the size in bytes
echo $size
