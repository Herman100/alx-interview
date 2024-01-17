#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const film = JSON.parse(body);
    printCharacters(film.characters, 0);
  }
});

function printCharacters(characters, i) {
  if (i >= characters.length) {
    return;
  }
  request(characters[i], function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(characters, i + 1);
    }
  });
}
