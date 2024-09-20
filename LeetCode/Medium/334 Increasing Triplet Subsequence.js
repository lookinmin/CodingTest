/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function (nums) {
  var first = Infinity;
  var second = Infinity;

  for (num of nums) {
    if (num <= first) {
      first = num;
    } else if (num <= second) {
      second = num;
    } else {
      return true;
    }
  }
  return false;
};
