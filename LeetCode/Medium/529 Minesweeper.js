/**
 * @param {character[][]} board
 * @param {number[]} click
 * @return {character[][]}
 */
var updateBoard = function (board, click) {
  // click = n, m
  const n = board.length;
  const m = board[0].length;

  let visited = Array.from(Array(n), () => Array(m).fill(0));
  const dx = [-1, -1, -1, 0, 1, 1, 1, 0];
  const dy = [-1, 0, 1, 1, 1, 0, -1, -1];

  const countMines = (x, y) => {
    let cnt = 0;
    for (let i = 0; i < 8; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (nx >= 0 && nx < n && ny >= 0 && ny < m && board[nx][ny] === 'M') {
        cnt++;
      }
    }
    return cnt;
  };
  const bfs = (x, y) => {
    if (board[x][y] === 'M') {
      board[x][y] = 'X';
      return;
    }

    const q = [];
    q.push([x, y]);
    visited[x][y] = 1;

    while (q.length > 0) {
      const [a, b] = q.shift();
      const num = countMines(a, b);

      if (num > 0) {
        board[a][b] = num.toString();
      } else {
        board[a][b] = 'B';
        for (let i = 0; i < 8; i++) {
          let nx = a + dx[i];
          let ny = b + dy[i];

          if (
            nx >= 0 &&
            nx < n &&
            ny >= 0 &&
            ny < m &&
            !visited[nx][ny] &&
            board[nx][ny] === 'E'
          ) {
            visited[nx][ny] = 1;
            q.push([nx, ny]);
          }
        }
      }
    }
  };

  bfs(click[0], click[1]);
  return board;
};
