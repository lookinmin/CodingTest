function solution(n, costs) {
  var graph = Array.from(Array(n), () => []);
  for (let [a, b, w] of costs) {
    graph[a].push([b, w]);
    graph[b].push([a, w]);
  }

  var visited = new Array(n).fill(false);
  const pq = [[0, 0]];
  // cost, nodeNum

  let total = 0;
  let edgeCnt = 0;

  while (pq.length > 0 && edgeCnt < n) {
    pq.sort((a, b) => a[0] - b[0]);
    const [cost, node] = pq.shift();

    if (visited[node]) continue;

    visited[node] = true;
    total += cost;
    edgeCnt++;

    for (let [nxtNode, nxtCost] of graph[node]) {
      if (!visited[nxtNode]) {
        pq.push([nxtCost, nxtNode]);
      }
    }
  }

  return total;
}
