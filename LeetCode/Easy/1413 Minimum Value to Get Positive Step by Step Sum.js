/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function (nums) {
  let psum = 0;
  let minSum = 0;

  for (let num of nums) {
    psum += num;
    minSum = Math.min(minSum, psum);
  }

  return 1 - minSum;
};
