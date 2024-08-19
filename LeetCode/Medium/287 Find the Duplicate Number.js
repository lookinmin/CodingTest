/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
  var tmp = new Set();
  for (num of nums) {
    if (tmp.has(num)) {
      return num;
    } else {
      tmp.add(num);
    }
  }
  return num;
};
