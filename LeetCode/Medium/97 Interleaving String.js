var isInterleave = function (s1, s2, s3) {
  if (s1.length + s2.length !== s3.length) return false;
  var n = s1.length;
  var m = s2.length;
  var dp = Array.from(Array(n + 1), () => Array(m + 1).fill(false));
  dp[0][0] = true;

  for (let i = 0; i <= n; i++) {
    for (let j = 0; j <= m; j++) {
      if (i > 0) {
        dp[i][j] = dp[i][j] || (dp[i - 1][j] && s1[i - 1] === s3[i + j - 1]);
      }
      if (j > 0) {
        dp[i][j] = dp[i][j] || (dp[i][j - 1] && s2[j - 1] === s3[i + j - 1]);
      }
    }
  }

  return dp[n][m];
};
