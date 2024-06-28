var input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
var n = Number(input[0])
var graph = new Array();
for(let i = 1; i<n + 1;i++){
    graph.push(input[i].split(' ').map(Number));
}

var visited = Array.from(Array(n), () => Array(n).fill(0));
const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

var res = 0

const dfs = (depth, x, y, sum) => {
    visited[x][y] = 1

    for(let i = 0;i<4;i++){
        var nx = x + dx[i]
        var ny = y + dy[i]
        if(0<=nx && nx < n && 0<=ny && ny < n && visited[nx][ny] === 0){
            visited[nx][ny] = 1
            var tmp = sum + graph[x][y] + graph[nx][ny]

            if(depth === 3 || (n < 3 && depth === 1)){
                res = Math.max(res, tmp)
                visited[nx][ny] = 0
                return
            }

            for(let i = 0; i < n;i++){
                for(let j = 0; j < n;j++){
                    if(visited[i][j] === 0){
                        dfs(depth + 1, i, j, tmp);
                        visited[i][j] = 0;
                    }
                }
            }
            visited[nx][ny] = 0;
        }
    }
}

for(let x = 0; x < n; x++){
    for(let y = 0; y < n;y++){
        dfs(0, x, y, 0);
        visited[x][y] = 0;
    }
}
console.log(res)