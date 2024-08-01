/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function (board) {
  var dx = [-1, 1, 0, 0, 1, -1, 1, -1];
  var dy = [0, 0, -1, 1, 1, -1, -1, 1];

  const n = board.length;
  const m = board[0].length;
  var tmp = Array.from(Array(n), () => Array(m).fill(0));

  const check = (x, y) => {
    var flag = true;
    if (board[x][y] === 0) {
      flag = false;
    } else {
      flag = true;
    }
    var cnt = 0;
    for (let i = 0; i < 8; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if (board[nx][ny] === 1) {
          cnt++;
        }
      }
    }

    if (flag) {
      // 1
      if (cnt === 2 || cnt === 3) {
        tmp[x][y] = 1;
      } else if (cnt > 3) {
        tmp[x][y] = 0;
      } else if (cnt < 2) {
        tmp[x][y] = 0;
      }
    } else {
      // 0
      if (cnt === 3) {
        tmp[x][y] = 1;
      } else {
        tmp[x][y] = 0;
      }
    }
  };

  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      check(x, y);
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      board[i][j] = tmp[i][j];
    }
  }
};
