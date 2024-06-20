#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

const fileA = process.argv[1];
const fileB = process.argv[2];
const fileC = process.argv[3];

try {
  const contentA = fs.readFileSync(fileA, 'utf8');
  const contentB = fs.readFileSync(fileB, 'utf8');
  const concatenatedContent = contentA + contentB;
  fs.writeFileSync(fileC, concatenatedContent);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
