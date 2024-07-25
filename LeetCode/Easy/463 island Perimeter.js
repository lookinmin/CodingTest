var islandPerimeter = function (grid) {
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  const n = grid.length;
  const m = grid[0].length;

  const check = (x, y) => {
    var tmp = 0;
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if (grid[nx][ny] === 0) {
          tmp++;
        }
      } else {
        tmp++;
      }
    }
    return tmp;
  };
  var total = 0;
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (grid[x][y] === 1) {
        total += check(x, y);
      }
    }
  }

  return total;
};
