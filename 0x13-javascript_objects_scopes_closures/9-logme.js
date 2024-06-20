#!/usr/bin/node
let numPrinted = 0; // Initialize the count of printed arguments

exports.logMe = function (item) {
  console.log(`${numPrinted}: ${item}`);
  numPrinted++; // Increment the count for the next argument
};
