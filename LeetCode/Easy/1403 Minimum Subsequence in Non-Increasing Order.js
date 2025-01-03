/**
 * @param {number[]} nums
 * @return {number[]}
 */
var minSubsequence = function (nums) {
  nums.sort((a, b) => b - a);
  let front = 0;
  let back = nums.reduce((acc, num) => acc + num, 0);
  let res = [];
  for (let num of nums) {
    front += num;
    back -= num;
    res.push(num);
    if (front > back) {
      return res;
    }
  }
};
