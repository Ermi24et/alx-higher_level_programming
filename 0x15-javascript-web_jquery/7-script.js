#!/usr/bin/node
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (query) {
    $('#character').text(query.name);
});