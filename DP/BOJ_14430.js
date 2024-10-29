// S2, 자원캐기
var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let [n, m] = input[0].split(' ').map(Number);
input.splice(0, 1);
let board = [];

for (let i = 0; i < n; i++) {
  board.push(input[i].split(' ').map(Number));
}

let dp = Array.from(Array(n), () => Array(m).fill(0));
dp[0][0] = board[0][0];

for (let x = 0; x < n; x++) {
  for (let y = 0; y < m; y++) {
    if (x === 0 && y === 0) {
      continue;
    }
    if (x === 0) {
      dp[x][y] = board[x][y] + dp[x][y - 1];
      continue;
    }
    if (y === 0) {
      dp[x][y] = board[x][y] + dp[x - 1][y];
      continue;
    }
    dp[x][y] = Math.max(dp[x - 1][y], dp[x][y - 1]) + board[x][y];
  }
}

console.log(dp[n - 1][m - 1]);
