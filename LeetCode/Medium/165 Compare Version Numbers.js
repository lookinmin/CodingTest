/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function (version1, version2) {
  var tmp1 = [];
  var tmp2 = [];

  for (let x of version1.split('.')) {
    tmp1.push(parseInt(x));
  }

  for (let x of version2.split('.')) {
    tmp2.push(parseInt(x));
  }

  const n = tmp1.length;
  const m = tmp2.length;
  let diff = Math.abs(n - m);

  if (n < m) {
    let temp = Array(diff).fill(0);
    tmp1.push(...temp);
  } else if (n > m) {
    let temp = Array(diff).fill(0);
    tmp2.push(...temp);
  }

  for (let i = 0; i < tmp1.length; i++) {
    if (tmp1[i] > tmp2[i]) {
      return 1;
    } else if (tmp1[i] < tmp2[i]) {
      return -1;
    }
  }
  return 0;
};
