#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request
request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
