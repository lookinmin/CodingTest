/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function (s, k) {
  const n = s.length;
  var start = 0;
  var res = '';
  while (start < n) {
    let end = Math.min(start + k, n);
    for (let i = end - 1; i >= start; i--) {
      res += s[i];
    }
    start = end;
    end = Math.min(start + k, n);
    for (let i = start; i < end; i++) {
      res += s[i];
    }
    start = end;
  }
  return res;
};
