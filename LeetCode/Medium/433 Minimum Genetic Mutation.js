/**
 * @param {string} startGene
 * @param {string} endGene
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function (startGene, endGene, bank) {
  const bfs = (s) => {
    var q = [];
    var visited = new Set();
    q.push([s, 0]);
    visited.add(s);

    while (q.length > 0) {
      let [now, value] = q.shift();
      if (now === endGene) {
        return value;
      }

      for (let w of bank) {
        if (!visited.has(w)) {
          let diff = 0;
          for (let i = 0; i < now.length; i++) {
            if (now[i] != w[i]) {
              diff++;
            }
          }
          if (diff === 1) {
            q.push([w, value + 1]);
            visited.add(w);
          }
        }
      }
    }
    return -1;
  };

  return bfs(startGene);
};
