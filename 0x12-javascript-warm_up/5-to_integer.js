#!/usr/bin/node
// a script that prints a converted string
const args = process.argv[2];
const parsedArg = parseInt(args);
if (!isNaN(parsedArg)) {
  console.log('My number: ' + parsedArg);
} else {
  console.log('Not a number');
}
