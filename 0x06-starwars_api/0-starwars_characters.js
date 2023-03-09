#!/usr/bin/env node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

// Wrapper function for request library
// makes it return a promise
function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, res, body) => {
      if (!error && res.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

async function getData (url) {
  try {
    // await expects a promise from doRequest
    const response = await doRequest(url);
    const characters = JSON.parse(response).characters;
    for (const characterUrl of characters) {
      const character = await doRequest(characterUrl);
      console.log(JSON.parse(character).name);
    }
  } catch (error) {
    console.log(error);
  }
}
getData(url);

