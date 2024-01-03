#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, function (error, response, body) {
  if (error) throw error;
  let i = 0;
  for (const film of JSON.parse(body).results) {
    for (const charac of film.characters) {
      if (charac.endsWith('/18/')) {
        i++;
      }
    }
  }
  console.log(i);
});
