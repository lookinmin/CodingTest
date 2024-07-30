/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
  var s = s.split('').sort();
  var t = t.split('').sort();

  for (let i = 0; i < s.length; i++) {
    if (s[i] !== t[i]) {
      return t[i];
    }
  }
  return t[t.length - 1];
};
