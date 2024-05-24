function solution(n, results) {
  var answer = 0;
  var winGraph = [];
  var loseGraph = [];

  results.forEach((res) => {
    let winner = res[0];
    let loser = res[1];
    if (winGraph[winner]) {
      winGraph[winner].push(loser);
    } else {
      winGraph[winner] = [loser];
    }

    if (loseGraph[loser]) {
      loseGraph[loser].push(winner);
    } else {
      loseGraph[loser] = [winner];
    }
  });

  const bfs = (graph, start) => {
    var visited = new Set();
    var q = [start];
    visited.add(start);

    let res = 0;

    while (q.length > 0) {
      const node = q.shift();
      for (let nxtNode of graph[node] || []) {
        if (!visited.has(nxtNode)) {
          visited.add(nxtNode);
          q.push(nxtNode);
          res++;
        }
      }
    }
    return res;
  };

  for (let v = 1; v <= n; v++) {
    if (bfs(winGraph, v) + bfs(loseGraph, v) === n - 1) {
      answer++;
    }
  }

  return answer;
}
