/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function (equations, values, queries) {
  // a / b = 2.0
  // b / c = 3.0
  let totalSet = new Set();
  let graph = new Map();

  for (let i = 0; i < equations.length; i++) {
    let [a, b] = equations[i];
    totalSet.add(a);
    totalSet.add(b);

    // 각 노드에 연결된 노드와 가중치를 배열로 추가
    if (!graph.has(a)) graph.set(a, []);
    if (!graph.has(b)) graph.set(b, []);

    graph.get(a).push([b, values[i]]);
    graph.get(b).push([a, 1 / values[i]]);
  }

  const dfs = (node, e, val, visited) => {
    if (node === e) {
      return val;
    }

    visited.add(node);

    for (let [v, w] of graph.get(node)) {
      if (!visited.has(v)) {
        const tmp = dfs(v, e, val * w, visited);
        if (tmp !== -1) {
          return tmp;
        }
      }
    }
    visited.delete(node);
    return -1;
  };

  const n = queries.length;
  let res = Array(n).fill(0.0);

  for (let i = 0; i < n; i++) {
    let [a, b] = queries[i];
    if (!totalSet.has(a) || !totalSet.has(b)) {
      res[i] = -1.0;
      continue;
    } else {
      let visited = new Set();
      res[i] = dfs(a, b, 1, visited);
    }
  }
  return res;
};
