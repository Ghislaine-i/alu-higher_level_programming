#!/usr/bin/node

// Import the required module
const request = require('request');

// Get the API URL from command line arguments
const url = process.argv[2];

// Make the GET request
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Parse the response body as JSON
    const todos = JSON.parse(body);
    const completedTasks = {};

    // Loop through the tasks
    todos.forEach((task) => {
      if (task.completed === true) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId]++;
      }
    });

    // Print the result as an object
    console.log(completedTasks);
  }
});
