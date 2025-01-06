/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParityII = function (nums) {
  const n = nums.length;
  var res = Array(n).fill(0);
  let even = 0;
  let odd = 1;

  for (let num of nums) {
    if (num % 2 === 0) {
      res[even] = num;
      even += 2;
    } else {
      res[odd] = num;
      odd += 2;
    }
  }
  return res;
};
