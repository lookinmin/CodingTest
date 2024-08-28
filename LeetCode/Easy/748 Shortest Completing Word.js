/**
 * @param {string} licensePlate
 * @param {string[]} words
 * @return {string}
 */
var shortestCompletingWord = function (licensePlate, words) {
  const isLP = licensePlate.toLowerCase().split('');
  var dic = {};
  for (let w of isLP) {
    if (/[a-z]/.test(w)) {
      // 알파벳만 처리
      if (dic[w]) {
        dic[w]++;
      } else {
        dic[w] = 1;
      }
    }
  }

  words.sort((a, b) => a.length - b.length);

  for (word of words) {
    var tmp = { ...dic };
    for (w of word) {
      if (tmp[w] > 0) {
        tmp[w]--;
      }
    }
    var sum = Object.values(tmp).reduce((acc, val) => acc + val, 0);
    if (sum === 0) {
      return word;
    }
  }
};
