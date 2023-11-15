#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const _id in dict) {
  const occurrences = dict[_id];
  if (occurrences in newDict) {
    newDict[occurrences].push(_id);
  } else {
    newDict[occurrences] = [_id];
  }
}
console.log(newDict);
