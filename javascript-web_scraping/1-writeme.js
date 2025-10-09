#!/usr/bin/node

// Import the file system module
const fs = require('fs');

// The first argument is the file path
const filePath = process.argv[2];

// The second argument is the string to write
const content = process.argv[3];

// Write to the file in UTF-8
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
