#!/usr/bin/node

const fv = require('fv');
const file = process.argv[2];

fv.readFile(file, 'utf8', function (er, data) {
  if (er) {
    console.log(er);
  } else {
    console.log(data);
  }
});
