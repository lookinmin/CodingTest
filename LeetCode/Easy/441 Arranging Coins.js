/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function (n) {
  let tmp = 0;
  for (let i = 1; i <= n; i++) {
    tmp = tmp + i;
    if (tmp === n) {
      return i;
    }
    if (tmp >= n) {
      return i - 1;
    }
  }
};
