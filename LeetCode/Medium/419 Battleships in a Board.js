/**
 * @param {character[][]} board
 * @return {number}
 */
var countBattleships = function (board) {
  const n = board.length;
  const m = board[0].length;
  var visited = Array.from(Array(n), () => Array(m).fill(0));
  const bfs = (a, b) => {
    var q = new Array();
    q.push([a, b]);
    visited[a][b] = 1;

    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    while (q.length > 0) {
      var [x, y] = q.shift();
      for (let i = 0; i < 4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];

        if (
          0 <= nx &&
          nx < n &&
          0 <= ny &&
          ny < m &&
          visited[nx][ny] === 0 &&
          board[nx][ny] === 'X'
        ) {
          q.push([nx, ny]);
          visited[nx][ny] = 1;
        }
      }
    }
    return;
  };
  var cnt = 0;
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (board[x][y] === 'X' && visited[x][y] === 0) {
        bfs(x, y);
        cnt++;
      }
    }
  }

  return cnt;
};
