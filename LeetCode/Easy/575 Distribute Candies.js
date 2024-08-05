/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function (candyType) {
  var n = candyType.length / 2;
  var tmp = new Set(candyType);
  if (n <= tmp.size) {
    return n;
  } else if (n > tmp.size) {
    return tmp.size;
  }
};
