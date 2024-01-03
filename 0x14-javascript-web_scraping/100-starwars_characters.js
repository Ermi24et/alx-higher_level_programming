#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(api, (error, response, body) => {
  if (error) throw error;
  for (const charac of JSON.parse(body).characters) {
    request(charac, (error, response, body) => {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  }
});
