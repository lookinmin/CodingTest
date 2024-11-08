/**
 * @param {number[][]} dominoes
 * @return {number}
 */
var numEquivDominoPairs = function (dominoes) {
  // N개 쌍 -> NC2 = n * (n - 1) / 2

  let cntPairs = new Map();

  for (let domino of dominoes) {
    let cvt = domino.sort((a, b) => a - b).join(',');
    cntPairs.set(cvt, (cntPairs.get(cvt) || 0) + 1);
  }

  let res = 0;
  for (let value of cntPairs.values()) {
    let tmp = Math.floor((value * (value - 1)) / 2);
    res += tmp;
  }

  return res;
};
