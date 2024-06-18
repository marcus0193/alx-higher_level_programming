#!/usr/bin/node
const firstArg = process.argv[2]; // Get the first argument

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
