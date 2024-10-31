/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function (str1, str2) {
  if (str1 + str2 !== str2 + str1) return '';

  let n = str1.length;
  let m = str2.length;

  while (m) {
    let tmp = m;
    m = n % m;
    n = tmp;
  }
  return str1.substring(0, n);
};
