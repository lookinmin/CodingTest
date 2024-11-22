/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function (n) {
  var res = [];
  let num = 1;

  if (n % 2 !== 0) {
    res.push(0);
  }

  for (let i = 0; i < Math.floor(n / 2); i++) {
    res.push(num);
    res.unshift(-num);
    num++;
  }

  return res;
};
