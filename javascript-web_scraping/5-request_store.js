#!/usr/bin/node

// Import the required modules
const request = require('request');
const fs = require('fs');

// Get the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Send GET request to the given URL
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Write the body content to the file in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
