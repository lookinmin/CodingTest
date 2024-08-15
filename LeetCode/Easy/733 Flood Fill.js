/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, color) {
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  const target = image[sr][sc];

  const n = image.length;
  const m = image[0].length;
  var res = Array.from(Array(n), () => Array(m).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      res[i][j] = image[i][j];
    }
  }
  if (target === color) {
    return res;
  }

  var visited = Array.from(Array(n), () => Array(m).fill(false));
  const bfs = (a, b, num) => {
    var q = [];
    visited[a][b] = true;
    q.push([a, b]);

    while (q.length > 0) {
      let [x, y] = q.shift();
      for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if (
          0 <= nx &&
          nx < n &&
          0 <= ny &&
          ny < m &&
          !visited[nx][ny] &&
          image[nx][ny] === num
        ) {
          q.push([nx, ny]);
          visited[nx][ny] = true;
        }
      }
    }
  };

  bfs(sr, sc, target);

  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (visited[x][y]) {
        res[x][y] = color;
      }
    }
  }
  return res;
};
