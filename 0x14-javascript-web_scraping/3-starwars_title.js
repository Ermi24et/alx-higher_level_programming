#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/' + parseInt(movieId);
request(api, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
