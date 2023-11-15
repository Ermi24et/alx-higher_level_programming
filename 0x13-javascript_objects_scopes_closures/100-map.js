#!/usr/bin/node
const { list } = require('./100-data.js');
const myList = list.map((value, index) => value * index);
console.log(list);
console.log(myList);
