/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function (num) {
  var binNum = num.toString(2);
  var cvt = '';
  for (let n of binNum) {
    if (n === '1') {
      cvt += '0';
    } else {
      cvt += '1';
    }
  }
  var res = parseInt(cvt, 2);
  return res;
};
