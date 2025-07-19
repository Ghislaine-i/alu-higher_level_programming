#!/bin/bash
# This script calculates the size of a URL's response body.
body_size_bytes=$(curl -s -o /dev/null -w "%{size_download}" "$1"); echo "Size of response body: ${body_size_bytes} bytes"
