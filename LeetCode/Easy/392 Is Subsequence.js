/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
  var idx = 0;
  if (s.length > t.length) {
    return false;
  }
  for (let w of s) {
    if (idx === t.length && t[idx] !== w) {
      return false;
    }
    for (let i = idx; i < t.length; i++) {
      if (t[i] === w) {
        idx = i + 1;
        break;
      }
      if (i === t.length - 1 && t[i] !== w) {
        return false;
      }
    }
  }
  return true;
};
