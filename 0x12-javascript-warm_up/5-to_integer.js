#!/usr/bin/node
const firstArg = process.argv[2];
const parsedInt = parseInt(firstArg, 10);

if (isNaN(parsedInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedInt}`);
}
