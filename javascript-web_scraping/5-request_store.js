#!/usr/bin/node

// Import the required modules
const request = require('request');
const fs = require('fs');

// Get arguments from command line
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    // Write the body content to the specified file (UTF-8)
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
