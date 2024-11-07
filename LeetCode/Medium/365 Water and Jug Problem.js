/**
 * @param {number} x
 * @param {number} y
 * @param {number} target
 * @return {boolean}
 */
var canMeasureWater = function (x, y, target) {
  if (target > x + y) {
    return false;
  }

  const getGCD = (minNum, maxNum) => {
    return minNum % maxNum === 0 ? maxNum : getGCD(maxNum, minNum % maxNum);
  };

  let big = Math.max(x, y);
  let small = Math.min(x, y);
  return target % getGCD(small, big) === 0;
};
