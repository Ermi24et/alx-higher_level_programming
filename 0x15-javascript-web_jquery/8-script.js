#!/usr/bin/node
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (query) {
    query.results.forEach(function (film) {
        $('#list_movies').append('<li>' + film.title + '</li>');
    });
});