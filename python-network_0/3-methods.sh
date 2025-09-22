#!/bin/bash
# This script displays all HTTP methods accepted by a URL.
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | cut -d' ' -f2-
