#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const stringTo = process.argv[3];
fs.writeFile(filePath, stringTo, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
