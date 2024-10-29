var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = parseInt(input[0]);
let stones = [];
for (let i = 1; i < n; i++) {
  let [small, big] = input[i].split(' ').map(Number);
  stones.push([small, big]);
}
const k = parseInt(input[n]);

// DP 배열 초기화
let dp = Array(n).fill(Infinity);
dp[0] = 0;

// 매우 큰 점프를 사용하지 않는 경우
for (let i = 1; i < n; i++) {
  if (i > 1) {
    dp[i] = Math.min(
      dp[i - 1] + stones[i - 1][0],
      dp[i - 2] + stones[i - 2][1],
      dp[i],
    );
  } else {
    dp[i] = Math.min(dp[i], dp[i - 1] + stones[i - 1][0]);
  }
}

// 매우 큰 점프를 사용한 경우의 최소값을 계산
let minEnergy = dp[n - 1]; // 매우 큰 점프를 사용하지 않은 최소 에너지

for (let i = 3; i < n; i++) {
  let tempDp = [...dp]; // 기존 dp를 복사하여 사용
  tempDp[i] = Math.min(tempDp[i], dp[i - 3] + k); // 매우 큰 점프를 사용

  // 매우 큰 점프 이후 남은 구간 계산
  for (let j = i + 1; j < n; j++) {
    if (j > i + 1) {
      tempDp[j] = Math.min(
        tempDp[j],
        tempDp[j - 1] + stones[j - 1][0],
        tempDp[j - 2] + stones[j - 2][1], // 큰 점프
      );
    } else {
      tempDp[j] = Math.min(
        tempDp[j],
        tempDp[j - 1] + stones[j - 1][0], // 작은 점프
      );
    }
  }

  minEnergy = Math.min(minEnergy, tempDp[n - 1]); // 최소값 갱신
}

console.log(minEnergy);
