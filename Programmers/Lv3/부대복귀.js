function solution(n, roads, sources, destination) {
  var answer = [];
  // start = destination
  var graph = Array.from(Array(n + 1), () => []);

  for (let [a, b] of roads) {
    graph[a].push(b);
    graph[b].push(a);
  }

  var start = destination;

  const bfs = (s) => {
    var q = [s];
    dist[s] = 0;

    while (q.length > 0) {
      var node = q.shift();

      for (let edj of graph[node]) {
        if (dist[edj] === -1) {
          dist[edj] = dist[node] + 1;
          q.push(edj);
        }
      }
    }
  };
  var dist = Array(n + 1).fill(-1);
  bfs(start);

  for (let end of sources) {
    answer.push(dist[end]);
  }

  return answer;
}
