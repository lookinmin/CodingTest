/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function (n) {
  // 이분탐색
  let small = 1;
  let big = n;
  while (small <= big) {
    let mid = Math.floor((small + big) / 2);
    const res = guess(mid);

    if (res === 0) {
      return mid;
    } else if (res === -1) {
      big = mid - 1;
    } else {
      small = mid + 1;
    }
  }
};
