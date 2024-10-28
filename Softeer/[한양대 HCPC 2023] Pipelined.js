var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let n = parseInt(input[0]);
let process = input[1].split(' ').map(Number);

process.sort((a, b) => a - b);
let res = process[n - 1] + n - 1;
console.log(res);
