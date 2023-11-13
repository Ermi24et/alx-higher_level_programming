#!/usr/bin/node
// a script that prints a message depending on command line arguments
const args = process.argv;
const len = args.length;
// javascripts command lines starts from 2
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else if (len > 3) {
  console.log('Arguments found');
}
