#!/usr/bin/node
// a scripts that calculates factorial of the first argument
function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
const num = parseInt(process.argv[2]);
if (!isNaN(num)) {
  console.log(factorial(num));
} else {
  console.log(factorial(0));
}
