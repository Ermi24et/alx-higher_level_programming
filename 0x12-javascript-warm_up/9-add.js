#!/usr/bin/node
// a scripts that adds two numbers from cmd line arguments
function add (a, b) {
  return a + b;
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
console.log(add(a, b));
