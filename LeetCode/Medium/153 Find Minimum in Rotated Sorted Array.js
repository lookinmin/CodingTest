/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  var start = 0;
  var end = nums.length - 1;

  while (start < end) {
    let mid = Math.floor((start + end) / 2);
    if (nums[mid] > nums[end]) {
      start = mid + 1;
    } else {
      end = mid;
    }
  }
  return nums[start];
};
