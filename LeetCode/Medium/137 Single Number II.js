/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  var counter = new Map();

  for (let num of nums) {
    counter.set(num, (counter.get(num) || 0) + 1);
  }

  for (let num of nums) {
    if (counter.get(num) === 1) {
      return num;
    }
  }
};
