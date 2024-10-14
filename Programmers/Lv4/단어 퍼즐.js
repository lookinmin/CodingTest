function solution(strs, t) {
  const n = t.length;
  const dp = new Array(n + 1).fill(Infinity);
  dp[0] = 0;

  for (let i = 1; i <= n; i++) {
    for (const str of strs) {
      if (i >= str.length && t.slice(i - str.length, i) === str) {
        dp[i] = Math.min(dp[i], dp[i - str.length] + 1);
      }
    }
  }

  return dp[n] === Infinity ? -1 : dp[n];
}
