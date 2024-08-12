/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function (nums) {
  const target = nums;
  const k = nums.length;

  if (k <= 1) {
    return;
  }

  var idx = k - 2;
  while (idx >= 0 && nums[idx] >= nums[idx + 1]) {
    idx--;
  }

  if (idx >= 0) {
    var j = k - 1;
    while (nums[j] <= nums[idx]) {
      j -= 1;
    }
    [nums[idx], nums[j]] = [nums[j], nums[idx]];
  }
  var tmp = nums.splice(idx + 1).reverse();
  nums.push(...tmp);
};
