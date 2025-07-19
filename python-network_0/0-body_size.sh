#!/bin/bash
URL="$1"; curl -s -o /dev/null -w "%{size_download}" "$URL"; echo "Size of response body: $(curl -s -o /dev/null -w "%{size_download}" "$URL") bytes"
