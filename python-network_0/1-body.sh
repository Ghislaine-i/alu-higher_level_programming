#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body
# of the response only if the HTTP status code is 200 OK, following redirects.
curl -sLf "$1"
