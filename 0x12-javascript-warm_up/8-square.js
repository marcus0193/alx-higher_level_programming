#!/usr/bin/node
const args = process.argv.slice(2);
const size = parseInt(process.argv[2], 10);

if (args.length === 0) {
  console.log('Missing size');
} else if (size > 0) {
  const line = 'X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(line);
  }
}
