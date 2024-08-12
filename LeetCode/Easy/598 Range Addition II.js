/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} ops
 * @return {number}
 */
var maxCount = function (n, m, ops) {
  if (ops.length === 0) {
    return n * m;
  }

  let minX = n;
  let minY = m;

  for (let [x, y] of ops) {
    minX = Math.min(x, minX);
    minY = Math.min(y, minY);
  }

  return minX * minY;
};
