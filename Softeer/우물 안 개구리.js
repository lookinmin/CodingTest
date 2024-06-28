var input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
var [n, m] = input[0].split(' ').map(Number);
var weights = [0, ...input[1].split(' ').map(Number)];
var graph = new Array(n + 1).fill().map(() => []);
input.splice(0, 2);

var cant = new Set();

for(let i = 0; i < m; i++){
    var [a, b] = input[i].split(' ').map(Number); 
    graph[a].push(b);
    graph[b].push(a);
}

const bfs = (v) => {
    for(node of graph[v]){
        if(weights[node] < weights[v]){
            cant.add(node);
            continue;
        } else if (weights[node] > weights[v]){
            cant.add(v);
            return false;
        } else {
            cant.add(v);
            cant.add(node);
            return false;
        }
    }
    return true;
}

var res = 0;
for(let node = 1; node <= n; node++){
    if(graph[node].length === 0){
        res += 1;
        continue;
    } else {
        if(cant.has(node) === false){
            if(bfs(node)){res += 1;}
        }
    }
}
console.log(res)

