#!/usr/bin/node
// a script that prints a text x times
const args = process.argv[2];
const parsedArg = parseInt(args);
if (!isNaN(parsedArg)) {
  for (let i = 0; i < parsedArg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
