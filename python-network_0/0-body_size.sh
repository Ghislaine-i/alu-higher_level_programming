#!/bin/bash
# Function to display usage
usage() {
  echo "Usage: $0 <URL>"
  echo "Sends a GET request to the specified URL and displays the size of the response body in bytes."
  exit 1
}

# Check if a URL is provided
if [ -z "$1" ]; then
  usage
fi

URL="$1"

echo "Requesting URL: $URL"

# Send a GET request to the URL and get only the body, then pipe to 'wc -c' to count bytes
# We use -s for silent mode (no progress meter or error messages)
# We use -o /dev/null to discard the body (not strictly needed for wc -c if we just want size)
# But a more robust way to get *only* the body and then pipe it to wc -c is to write it to stdout.
# A simpler and more common approach for just getting the size:
# Use -w "%{size_download}" to extract the download size directly from curl's output
# This size includes the body, and potentially other downloaded content depending on context,
# but for a simple GET request of a single resource, it represents the body size.

# Method 1: Using -w "%{size_download}" (recommended for simplicity and directness)
# This directly extracts the size of the downloaded body from curl's internal variables.
body_size_bytes=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

# Method 2: Piping body to wc -c (alternative, good for conceptual understanding of body pipe)
# curl -s "$URL" | wc -c
# This method can be slightly less efficient as it actually downloads the body to pipe it.
# The `size_download` variable from `curl -w` is often preferred for just getting the size.


if [ $? -eq 0 ]; then
  echo "Size of response body: ${body_size_bytes} bytes"
else
  echo "Error: Could not retrieve response from $URL"
  exit 1
fi
