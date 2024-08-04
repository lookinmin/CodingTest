/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  const k = nums.length;
  if (k === 1) {
    return nums[0];
  }
  var dp = Array(k).fill(0);
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < k; i++) {
    dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1] + 0);
  }
  return dp[k - 1];
};
