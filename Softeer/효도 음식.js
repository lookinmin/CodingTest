const fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = parseInt(input[0]);
let ingredients = input[1].split(' ').map(Number);

if (n === 3) {
  console.log(ingredients[0] + ingredients[2]);
  process.exit(0);
}

var dp = new Array(n).fill(0);
var rdp = new Array(n).fill(0);
for (let i = 0; i < n; i++) {
  dp[i] = ingredients[i];
  rdp[i] = ingredients[i];
}

for (let i = 1; i < n; i++) {
  dp[i] = Math.max(dp[i], dp[i - 1] + ingredients[i]);
}

for (let i = n - 2; i > 0; i--) {
  rdp[i] = Math.max(rdp[i], rdp[i + 1] + ingredients[i]);
}

let psum = Array(n).fill(0);
psum[0] = dp[0];
let reversePsum = Array(n).fill(0);
reversePsum[n - 1] = rdp[n - 1];

for (let i = 1; i < n; i++) {
  psum[i] = Math.max(psum[i - 1], dp[i]);
}
for (let i = n - 2; i > 0; i--) {
  reversePsum[i] = Math.max(reversePsum[i + 1], rdp[i]);
}

var res = -Infinity;
for (let i = 1; i < n - 1; i++) {
  res = Math.max(res, psum[i - 1] + reversePsum[i + 1]);
}

console.log(res);
