#!/usr/bin/node

// Import the filesystem module
const fs = require('fs');

// Get the file path from the first argument
const filePath = process.argv[2];

// Read the file content in UTF-8
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
