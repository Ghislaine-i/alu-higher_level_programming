#!/bin/bash
# This script takes a URL as an argument, sends a GET request to it using curl,
# and displays the body of the response ONLY if the HTTP status code is 200.

# Check if a URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Use curl to send a GET request and capture both the HTTP status code
# and the response body.
# -s: Silent mode (don't show progress meter or error messages).
# -w "\n%{http_code}": This custom write-out format prints a newline,
#                       followed by the HTTP status code. This ensures the
#                       status code is on a new line at the very end of the output.
# The actual response body will be printed before this custom string.
RESPONSE=$(curl -s -w "\n%{http_code}" "$URL")

# Extract the HTTP status code, which is the last line of the RESPONSE.
HTTP_STATUS=$(echo "$RESPONSE" | tail -n 1)

# Extract the response body, which is everything except the last line.
# head -n -1 means "print all lines except the last 1".
BODY=$(echo "$RESPONSE" | head -n -1)

# Check if the extracted HTTP status code is 200.
if [ "$HTTP_STATUS" -eq 200 ]; then
    # If it's 200, print the captured body.
    echo "$BODY"
fi
