/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function (nums) {
  var sum = nums.reduce((a, b) => a + b, 0);
  if (sum % 2 !== 0) {
    return false;
  }

  const target = sum / 2;
  var dp = new Set([0]);

  for (let num of nums) {
    const newSums = new Set();

    for (const sum of dp) {
      if (sum + num === target) return true;
      if (sum + num < target) newSums.add(num + sum);
    }

    for (const sum of newSums) {
      dp.add(sum);
    }
  }

  return false;
};
