/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function (words, chars) {
  const k = chars.length;
  let res = '';

  let map = new Map();
  for (let c of chars) {
    map.set(c, (map.get(c) || 0) + 1);
  }

  for (word of words) {
    if (word.length > k) {
      continue;
    }
    let tmp = new Map([...map]);
    let flag = true;
    for (let w of word) {
      if (tmp.has(w) && tmp.get(w) > 0) {
        tmp.set(w, tmp.get(w) - 1);
      } else {
        flag = false;
        break;
      }
    }

    if (flag) {
      res += word;
    }
  }

  return res.length;
};
