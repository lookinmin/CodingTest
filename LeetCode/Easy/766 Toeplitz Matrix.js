/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var isToeplitzMatrix = function (matrix) {
  const n = matrix.length;
  const m = matrix[0].length;

  for (let x = 0; x < n - 1; x++) {
    for (let y = 0; y < m - 1; y++) {
      if (matrix[x][y] !== matrix[x + 1][y + 1]) return false;
    }
  }
  return true;
};
