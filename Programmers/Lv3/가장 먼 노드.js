function solution(n, edge) {
  // start = 1
  var answer = 0;
  var graph = Array.from(Array(n + 1), () => Array());

  for (v of edge) {
    let a = v[0];
    let b = v[1];
    graph[a].push(b);
    graph[b].push(a);
  }

  var visited = new Set();
  var dist = new Array(n + 1).fill(0);
  const bfs = () => {
    var q = [1];
    visited.add(1);

    while (q.length > 0) {
      let node = q.shift();

      graph[node].forEach((v) => {
        if (!visited.has(v)) {
          q.push(v);
          visited.add(v);
          dist[v] = dist[node] + 1;
        }
      });
    }
  };

  bfs();
  const maxVal = Math.max(...dist);
  for (num of dist) {
    if (num == maxVal) {
      answer += 1;
    }
  }
  return answer;
}
