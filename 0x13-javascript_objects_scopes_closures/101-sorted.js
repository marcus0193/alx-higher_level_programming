#!/usr/bin/node
const { dict } = require('./101-data');

// Initialize an empty object for the new dictionary
const userOccurrences = {};

// Iterate through the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!userOccurrences[occurrences]) {
    userOccurrences[occurrences] = [];
  }
  userOccurrences[occurrences].push(userId);
}

// Print the new dictionary
console.log(userOccurrences);
