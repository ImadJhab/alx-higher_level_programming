#!/usr/bin/node
const args = process.argv.slice(2);
const numb = Number(args[0]);
if (Number.isNaN(numb)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numb}`);
}
