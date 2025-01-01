/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function (mat, k) {
  let nums = [];
  for (let i = 0; i < mat.length; i++) {
    let cnt = 0;
    for (let j = 0; j < mat[0].length; j++) {
      if (mat[i][j] === 1) {
        cnt++;
      }
    }
    nums.push([cnt, i]);
  }
  nums.sort((a, b) => (a[0] - b[0]) | (a[1] - b[1]));
  var res = [];
  for (let i = 0; i < k; i++) {
    res.push(nums[i][1]);
  }
  return res;
};
