/**
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function (s) {
  let stack = [];
  let idxs = [];
  for (let i = 0; i < s.length; i++) {
    let w = s[i];
    if (
      ('a'.charCodeAt() <= w.charCodeAt() &&
        w.charCodeAt() <= 'z'.charCodeAt()) ||
      ('A'.charCodeAt() <= w.charCodeAt() && w.charCodeAt() <= 'Z'.charCodeAt())
    ) {
      stack.unshift(w);
    } else {
      idxs.push([i, w]);
    }
  }
  var res = '';
  for (let cnt = 0; cnt < s.length; cnt++) {
    if (idxs.length > 0) {
      if (cnt === idxs[0][0]) {
        res += idxs[0][1];
        idxs.shift();
      } else {
        res += stack[0];
        stack.shift();
      }
    } else {
      res += stack[0];
      stack.shift();
    }
  }

  return res;
};
