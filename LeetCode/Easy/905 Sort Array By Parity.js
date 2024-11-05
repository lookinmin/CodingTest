/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function (nums) {
  let res = [];

  for (let num of nums) {
    if (num % 2 === 0) {
      res.unshift(num);
    } else {
      res.push(num);
    }
  }

  return res;
};
