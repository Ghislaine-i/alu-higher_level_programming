#!/usr/bin/node

// Import the file system module
const fs = require('fs');

// The first argument (after the script name) is the file path
const filePath = process.argv[2];

// Read the file in UTF-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
