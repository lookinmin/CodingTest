var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim();
input = input.split('');
var res = '';
for (let i = 0; i < input.length - 1; i++) {
  if (input[i] === '(' && input[i + 1] === ')') {
    res += '(1)';
  } else if (input[i] === ')' && input[i + 1] === '(') {
    res += '+';
  } else {
    res += input[i];
  }
}

console.log(res);
