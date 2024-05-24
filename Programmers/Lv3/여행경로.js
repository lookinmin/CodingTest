function solution(tickets) {
  var k = tickets.length;

  var graph = {};

  for (ticket of tickets) {
    let start = ticket[0];
    let end = ticket[1];
    if (start in graph) {
      graph[start].push(end);
    } else [(graph[start] = [end])];
  }
  Object.keys(graph).forEach((e) => graph[e].sort());
  // console.log(graph)

  var route = [];
  const dfs = (node) => {
    while (graph[node] && graph[node].length > 0) {
      var nxt = graph[node].shift();
      dfs(nxt);
    }
    route.push(node);
  };

  dfs("ICN");
  return route.reverse();
}
