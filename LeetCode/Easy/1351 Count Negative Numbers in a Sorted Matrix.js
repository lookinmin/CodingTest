/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function (grid) {
  let n = grid.length;
  let x = 0,
    y = grid[0].length - 1;

  let res = 0;
  while (y >= 0 && x < n) {
    if (grid[x][y] < 0) {
      res += n - x;
      y--;
    } else {
      x++;
    }
  }
  return res;
};
