/**
 * @param {string} s
 * @param {character} c
 * @return {number[]}
 */
var shortestToChar = function (s, c) {
  var res = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === c) {
      res.push(0);
    } else {
      let right = Infinity;
      let left = Infinity;
      for (let j = i; j < s.length; j++) {
        if (s[j] === c) {
          right = j;
          break;
        }
      }
      for (let j = i; j >= 0; j--) {
        if (s[j] === c) {
          left = j;
          break;
        }
      }
      res.push(Math.min(Math.abs(right - i), Math.abs(i - left)));
    }
  }
  return res;
};
