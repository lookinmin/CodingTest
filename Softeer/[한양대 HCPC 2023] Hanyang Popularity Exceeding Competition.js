const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = parseInt(input[0]);
input.splice(0, 1);

let x = 0;
let celebs = [];
for (let i = 0; i < n; i++) {
  let [p, c] = input[i].split(' ').map(Number);
  celebs.push([p, c]);
}

// DP 배열 초기화
let dp = Array(n + 1).fill(0);

// DP 점화식으로 최대 인기도 계산
for (let i = 1; i <= n; i++) {
  // 현재 유명인을 만나지 않는 경우 (이전의 최대 인기도 유지)
  dp[i] = dp[i - 1];

  // 현재 유명인을 만날 경우 조건 체크
  if (Math.abs(celebs[i - 1][0] - x) <= celebs[i - 1][1]) {
    dp[i] = Math.max(dp[i], dp[i - 1] + 1); // 만나는 경우의 최댓값 선택
    x++; // 인기도 증가
  }
}

console.log(dp[n]);
