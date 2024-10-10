/**
 * @param {number[]} widths
 * @param {string} s
 * @return {number[]}
 */
var numberOfLines = function (widths, s) {
  let start = 'a'.charCodeAt();
  let end = 'z'.charCodeAt();

  var dict = {};

  for (let i = start; i <= end; i++) {
    dict[String.fromCharCode(i)] = widths[i - start];
  }

  let limit = 100;
  let line = 1;
  for (let w of s) {
    if (limit - dict[w] >= 0) {
      limit -= dict[w];
    } else {
      limit = 100;
      line++;
      limit -= dict[w];
    }
  }

  return [line, 100 - limit];
};
