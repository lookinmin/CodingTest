/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function (n) {
  if (n === 1) return 1;

  var dp = new Array(n);
  dp[0] = 1;
  let p1 = 0,
    p2 = 0,
    p3 = 0;
  for (let i = 1; i < n; i++) {
    let nxt1 = dp[p1] * 2;
    let nxt2 = dp[p2] * 3;
    let nxt3 = dp[p3] * 5;

    dp[i] = Math.min(nxt1, nxt2, nxt3);

    if (dp[i] === nxt1) p1++;
    if (dp[i] === nxt2) p2++;
    if (dp[i] === nxt3) p3++;
  }
  return dp[n - 1];
};
