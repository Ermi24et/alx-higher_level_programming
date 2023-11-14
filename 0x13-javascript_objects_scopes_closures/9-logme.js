#!/usr/bin/node
let k = 0;
exports.logMe = function (item) {
  console.log(`${k++}: ${item}`);
};
