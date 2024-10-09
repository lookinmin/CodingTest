/**
 * @param {number} n
 * @return {number}
 */
var lastRemaining = function (n) {
  let now = 1;
  let step = 1;
  let remain = n;
  let flag = true; // ->

  while (remain > 1) {
    if (flag || remain % 2 !== 0) {
      now += step;
    }
    remain = Math.floor(remain / 2);

    step *= 2;
    flag = !flag;
  }

  return now;
};
