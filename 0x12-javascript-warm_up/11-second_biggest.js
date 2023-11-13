#!/usr/bin/node
// a script that prints the second maximum number of an array
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  args.sort(function (a, b) { return b - a; });
  console.log(args[1]);
}
