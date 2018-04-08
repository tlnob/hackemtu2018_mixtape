
fs = require('fs')

const redline = require('readline');

fs.readFile('routes.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});