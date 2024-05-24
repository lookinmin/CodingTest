function solution(maps) {
  var answer = [];
  var n = maps.length;
  var m = maps[0].length;
  var visited = Array.from(Array(n), () => Array(m).fill(0));

  const bfs = (a, b) => {
    var k = parseInt(maps[a][b]);
    var q = [[a, b]];
    visited[a][b] = 1;

    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    var cnt = k;

    while (q.length > 0) {
      const [x, y] = q.shift();

      for (let i = 0; i < 4; i++) {
        var nx = x + dx[i];
        var ny = y + dy[i];

        if (
          0 <= nx &&
          nx < n &&
          0 <= ny &&
          ny < m &&
          visited[nx][ny] == 0 &&
          maps[nx][ny] !== "X"
        ) {
          q.push([nx, ny]);
          visited[nx][ny] = 1;
          cnt += parseInt(maps[nx][ny]);
        }
      }
    }
    return cnt;
  };

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (maps[i][j] !== "X" && visited[i][j] == 0) {
        answer.push(bfs(i, j));
      }
    }
  }
  return answer.length > 0 ? answer.sort((a, b) => a - b) : [-1];
}
