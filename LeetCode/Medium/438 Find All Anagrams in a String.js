/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function (s, p) {
  const n = s.length;
  const m = p.length;

  if (n < m) return [];

  var res = [];
  const aCharCode = 'a'.charCodeAt();

  const pCount = new Array(26).fill(0);
  const sCount = new Array(26).fill(0);

  for (let i = 0; i < m; i++) {
    pCount[p[i].charCodeAt() - aCharCode]++;
    sCount[s[i].charCodeAt() - aCharCode]++;
  }

  if (sCount.join('') === pCount.join('')) {
    res.push(0);
  }

  for (let i = m; i < n; i++) {
    sCount[s[i].charCodeAt() - aCharCode]++;
    sCount[s[i - m].charCodeAt() - aCharCode]--;

    if (sCount.join('') === pCount.join('')) {
      res.push(i - m + 1);
    }
  }

  return res;
};
