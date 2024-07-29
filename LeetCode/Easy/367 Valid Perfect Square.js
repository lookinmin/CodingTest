/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function (num) {
  if (Number.isInteger(Math.sqrt(num))) {
    return true;
  } else {
    return false;
  }
};
