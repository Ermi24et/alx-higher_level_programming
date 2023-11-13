#!/usr/bin/node
// a script that prints a square
const args = process.argv[2];
const parsedArg = parseInt(args);
if (!isNaN(parsedArg)) {
  for (let i = 0; i < parsedArg; i++) {
    let sq = '';
    for (let i = 0; i < parsedArg; i++) {
      sq += 'X';
    }
    console.log(sq);
  }
} else {
  console.log('Missing size');
}
