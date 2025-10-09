#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Define the API endpoint URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
