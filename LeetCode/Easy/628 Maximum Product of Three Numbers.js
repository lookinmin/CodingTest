/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function (nums) {
  var nums = nums.sort((a, b) => b - a);
  var k = nums.length;
  let res1 = nums[0] * nums[1] * nums[2];
  let res2 = nums[0] * nums[k - 1] * nums[k - 2];
  return res1 > res2 ? res1 : res2;
};
