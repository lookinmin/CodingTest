/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function (nums) {
  if (nums.length === 1) {
    return 0;
  }

  for (let idx = 0; idx < nums.length; idx++) {
    if (idx === 0) {
      if (nums[idx] > nums[idx + 1]) {
        return idx;
      }
    } else if (idx === nums.length - 1) {
      if (nums[idx] > nums[idx - 1]) {
        return idx;
      }
    } else {
      if (nums[idx] > nums[idx - 1] && nums[idx] > nums[idx + 1]) {
        return idx;
      }
    }
  }
};
