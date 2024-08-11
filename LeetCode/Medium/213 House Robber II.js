/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  const k = nums.length;
  if (k === 1) {
    return nums[0];
  } else if (k === 2) {
    return Math.max(nums[0], nums[1]);
  }

  const rob = (arr) => {
    const k = arr.length;
    var dp = Array(k).fill(0);

    dp[0] = arr[0];
    dp[1] = Math.max(arr[0], arr[1]);

    for (let i = 2; i < k; i++) {
      dp[i] = Math.max(dp[i - 2] + arr[i], dp[i - 1]);
    }
    return dp[k - 1];
  };

  var case1 = rob(nums.slice(0, k - 1));
  // 마지막 집 X
  var case2 = rob(nums.slice(1));
  // 첫번째 집 X, 마지막 집 O

  return Math.max(case1, case2);
};
