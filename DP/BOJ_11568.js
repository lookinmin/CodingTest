var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
n = parseInt(input[0]);
cards = input[1].split(' ').map(Number);

let dp = Array(n).fill(1);
for (let i = 1; i < n; i++) {
  for (let j = 0; j < i; j++) {
    if (cards[i] > cards[j]) {
      dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
}

console.log(Math.max(...dp));
