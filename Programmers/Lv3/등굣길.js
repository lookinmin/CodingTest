function solution(m, n, puddles) {
  // 1. n x m 크기의 배열을 1로 초기화
  let dp = Array.from(Array(n + 1), () => Array(m + 1).fill(0));
  dp[1][1] = 1;
  // 2. 웅덩이 처리
  for (let [x, y] of puddles) {
    dp[y][x] = -1; // 웅덩이 위치는 0으로 설정
  }

  // 3. 경로 계산
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      if (i === 1 && j === 1) continue;
      if (dp[i][j] === -1) {
        dp[i][j] = 0;
      } else {
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007;
      }
    }
  }

  return dp[n][m]; // 마지막 칸의 값 반환
}
