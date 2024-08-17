/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function (pattern, s) {
  var tmp = {};
  const k = pattern.length;
  var usedWords = new Set();
  var cvt = s.split(' ');

  if (k !== cvt.length) {
    return false;
  }

  for (let i = 0; i < k; i++) {
    if (tmp[pattern[i]]) {
      if (tmp[pattern[i]] !== cvt[i]) {
        return false;
      }
    } else {
      if (usedWords.has(cvt[i])) {
        return false;
      }
      tmp[pattern[i]] = cvt[i];
      usedWords.add(cvt[i]);
    }
  }
  return true;
};
