/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function (s) {
  let res = '';
  let cnt = 0;

  for (w of s) {
    if (w === '(') {
      if (cnt) res += w;
      cnt++;
    } else {
      cnt--;
      if (cnt) res += w;
    }
  }

  return res;
};
