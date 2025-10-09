#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the API URL from the command-line argument
const apiUrl = process.argv[2];

// Make a GET request to the provided API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;

    // Loop through all movies and check characters
    for (const film of data) {
      for (const character of film.characters) {
        if (character.includes('/18/')) {
          count++;
          break; // Count only once per film
        }
      }
    }

    console.log(count);
  }
});
