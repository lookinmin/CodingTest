/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
  var wordDic = new Map();
  for (let w of ransomNote) {
    wordDic.set(w, (wordDic.get(w) || 0) + 1);
  }

  for (let m of magazine) {
    if (wordDic.has(m) && wordDic.get(m) > 0) {
      wordDic.set(m, wordDic.get(m) - 1);
    }
  }

  let tmp = [...wordDic.values()];

  for (let num of tmp) {
    if (num > 0) {
      return false;
    }
  }

  return true;
};
