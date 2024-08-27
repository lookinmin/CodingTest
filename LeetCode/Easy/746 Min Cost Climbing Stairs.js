/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) {
  const k = cost.length;
  if (k === 0) return 0;
  if (k === 1) return cost[0];

  var dp0 = cost[0];
  var dp1 = cost[1];

  for (let i = 2; i < k; i++) {
    let cur = cost[i] + Math.min(dp0, dp1);
    [dp0, dp1] = [dp1, cur];
  }
  return Math.min(dp0, dp1);
};
