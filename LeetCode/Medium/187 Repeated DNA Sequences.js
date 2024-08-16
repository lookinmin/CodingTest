/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function (s) {
  var tmp = new Set();
  var res = new Set();
  if (s.length < 10) {
    return [];
  }

  for (let i = 0; i < s.length - 9; i++) {
    let now = s.slice(i, i + 10);
    if (tmp.has(now)) {
      res.add(now);
    } else {
      tmp.add(now);
    }
  }

  return [...res];
};
