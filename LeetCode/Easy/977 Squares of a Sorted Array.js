/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function (nums) {
  const n = nums.length;
  let res = new Array(n).fill(0);
  let left = 0;
  let right = n - 1;

  for (let i = n - 1; i >= 0; i--) {
    if (Math.abs(nums[left]) > Math.abs(nums[right])) {
      // 큰수부터 채우기
      res[i] = nums[left] ** 2;
      left++;
    } else {
      res[i] = nums[right] ** 2;
      right--;
    }
  }
  return res;
};
