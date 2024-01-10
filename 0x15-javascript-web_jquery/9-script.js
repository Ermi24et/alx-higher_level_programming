#!/usr/bin/node
$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (query) {
    $('#hello').text(query.hello);
});