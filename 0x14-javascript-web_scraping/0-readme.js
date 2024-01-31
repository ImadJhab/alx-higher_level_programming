#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  process.exitCode = 1;
} else {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      process.exitCode = 1;
      process.stdout.write(`${err}`);
    } else {
      process.stdout.write(`${data}`);
    }
  });
}
