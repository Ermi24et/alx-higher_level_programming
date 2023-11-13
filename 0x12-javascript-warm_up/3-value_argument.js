#!/usr/bin/node
// a script that prints the first argument passed to it
function funLength (args) {
  let count = 0;
  for (const i in args) {
    if (args[i] !== undefined) {
      count++;
    }
  }
  return count;
}
const args = process.argv;
const len = funLength(args);
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log(args[2]);
}
