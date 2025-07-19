 #!/bin/bash
# script takes a URL as an argument, sends a request to it using curl,
# and displays the size of the body of the response in bytes.

# Check if a URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Assign the first argument to a variable for clarity
URL=$1

# Use curl to send a request and get the response body size.
# -s: Silent mode. Don't show progress meter or error messages.
# -o /dev/null: Redirect the output body to /dev/null (discard it).
# -w "%{size_download}\n": Print only the size of the downloaded body in bytes,
#                          followed by a newline.
curl -s -o /dev/null -w "%{size_download}\n" "$URL"

