/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
  jewels = jewels.split('');
  var cnt = 0;
  for (let w of stones) {
    if (jewels.includes(w)) {
      cnt++;
    }
  }

  return cnt;
};
