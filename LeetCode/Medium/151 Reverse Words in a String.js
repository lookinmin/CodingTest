/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  var cvt = s.split(' ');
  console.log(cvt);
  cvt.reverse();
  var res = [];
  for (let word of cvt) {
    if (word !== '') {
      res.push(word);
    }
  }
  return res.join(' ').trim();
};
