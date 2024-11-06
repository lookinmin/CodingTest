/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function (s) {
  let freqMap = new Map();
  for (let w of s) {
    freqMap.set(w, (freqMap.get(w) || 0) + 1);
  }

  let cvt = [...freqMap];
  // let cvt = Array.from(freqMap);

  cvt.sort((a, b) => b[1] - a[1]);
  let res = '';
  cvt.forEach((e) => {
    res += e[0].repeat(e[1]);
  });
  return res;
};
