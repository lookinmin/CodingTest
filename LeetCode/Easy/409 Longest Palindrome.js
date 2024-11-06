/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  if (s.length === 1) {
    return 1;
  }
  var wordMap = new Map();

  for (let w of s) {
    wordMap.set(w, (wordMap.get(w) || 0) + 1);
  }

  let oneFlag = true;
  let res = 0;
  for (let [key, value] of wordMap) {
    if (value % 2 === 0) {
      res += value;
      continue;
    } else {
      if (oneFlag) {
        res += value;
        oneFlag = false;
      } else {
        res += value - 1;
      }
    }
  }

  return res;
};
