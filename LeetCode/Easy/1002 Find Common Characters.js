/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function (words) {
  let start = Array.from(words[0]).reduce((acc, char) => {
    acc[char] = (acc[char] || 0) + 1;
    return acc;
  }, {});

  for (let i = 1; i < words.length; i++) {
    let curWordFreq = Array.from(words[i]).reduce((acc, char) => {
      acc[char] = (acc[char] || 0) + 1;
      return acc;
    }, {});

    for (let ch in start) {
      if (curWordFreq[ch]) {
        start[ch] = Math.min(start[ch], curWordFreq[ch]);
      } else {
        delete start[ch];
      }
    }
  }

  let res = [];
  for (let w in start) {
    res.push(...Array(start[w]).fill(w));
  }
  return res;
};

// ----------------------------------- More Faster

var commonChars = function (words) {
  let result = [];
  for (let key of words[0]) {
    if (words.every((word) => word.includes(key))) {
      result.push(key);
      words = words.map((word) => word.replace(key, ''));
    }
  }

  return result;
};
