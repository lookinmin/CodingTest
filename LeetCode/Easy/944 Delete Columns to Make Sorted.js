/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function (strs) {
  const n = strs.length;
  const m = strs[0].length;
  var cnt = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (strs[j][i].charCodeAt() < strs[j - 1][i].charCodeAt()) {
        cnt++;
        break;
      }
    }
  }

  return cnt;
  // .charCodeAt, String.fromCharCode()
};
