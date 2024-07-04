#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the response body size using curl
response=$(curl -sI "$1" | grep -i Content-Length)
size=$(echo "$response" | awk '{print $2}')

# Display the size in bytes
echo $size
