var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var [n, m] = input[0].split(' ').map(Number);

input.splice(0, 1);
var board = Array();
for (let i = 0; i < n; i++) {
  board.push(input[i].split(' ').map(Number));
}
input.splice(0, n);
let [firstStart, firstEnd] = input[0].split(' ').map(Number);
let [ss, se] = input[1].split(' ').map(Number);

for (let idx = firstStart - 1; idx < firstEnd; idx++) {
  for (let k = 0; k < m; k++) {
    if (board[idx][k] === 1) {
      board[idx][k] = 0;
      break;
    }
  }
}

for (let idx = ss - 1; idx < se; idx++) {
  for (let k = 0; k < m; k++) {
    if (board[idx][k] === 1) {
      board[idx][k] = 0;
      break;
    }
  }
}
var res = 0;
for (let x = 0; x < n; x++) {
  for (let y = 0; y < m; y++) {
    if (board[x][y] === 1) {
      res++;
    }
  }
}
console.log(res);
