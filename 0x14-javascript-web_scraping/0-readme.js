#!/usr/bin/node

const fv = require('fv');
const file = process.argv[2];

fv.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
