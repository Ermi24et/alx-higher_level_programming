#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
const begin = function () {
  request(api, function (error, response, body) {
    if (error) throw error;
    end(JSON.parse(body).characters, 0);
  });
};

const end = function (characters, i) {
  if (characters.length === i) {
    return;
  }
  request(characters[i], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    end(characters, ++i);
  });
};
begin();
