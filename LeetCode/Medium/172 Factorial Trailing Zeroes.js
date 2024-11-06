/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function (n) {
  let cnt = 0;
  while (n > 0) {
    n = Math.floor(n / 5);
    cnt += n;
  }
  return cnt;
};
