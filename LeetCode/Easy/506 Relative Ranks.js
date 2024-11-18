/**
 * @param {number[]} score
 * @return {string[]}
 */
var findRelativeRanks = function (score) {
  let idx_arr = [];
  for (let i = 0; i < score.length; i++) {
    idx_arr.push([score[i], i]);
  }

  idx_arr.sort((a, b) => b[0] - a[0]);

  let res = Array(score.length).fill('');
  //console.log(idx_arr);
  var cnt = 1;
  for (let i = 0; i < idx_arr.length; i++) {
    let [val, pos] = idx_arr[i];
    if (cnt == 1) {
      res[pos] = 'Gold Medal';
    } else if (cnt == 2) {
      res[pos] = 'Silver Medal';
    } else if (cnt == 3) {
      res[pos] = 'Bronze Medal';
    } else {
      res[pos] = cnt.toString();
    }
    cnt++;
  }
  return res;
};
