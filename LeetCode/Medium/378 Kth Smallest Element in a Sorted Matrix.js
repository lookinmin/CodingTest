/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (matrix, k) {
  var cnt = 1;
  const n = matrix.length;
  var arr = [];
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      arr.push(matrix[i][j]);
    }
  }

  arr.sort((a, b) => a - b);
  return arr[k - 1];
};
