var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var n = Number(input[0])
input.splice(0, 1)

var graph = new Array();
for(let i=0;i<n;i++){
    var lst = input[i].split('').map(Number);
    graph.push(lst)
}
var visited = Array.from(Array(n), () => Array(n).fill(0))


const dx = [-1, 1, 0, 0]
const dy = [0, 0, -1, 1]

const bfs = (a, b) => {
    var q = [[a, b]];
    visited[a][b] = 1;
    const value = graph[a][b];
    var tmp = 1;
    while(q.length > 0){
        var [x, y] = q.shift();

        for(let i = 0; i < 4; i++){
            var nx = x + dx[i];
            var ny = y + dy[i];
            if(0<=nx && nx < n && 0<=ny && ny<n && visited[nx][ny] === 0 && graph[nx][ny] === value){
                q.push([nx,ny])
                visited[nx][ny] = 1;
                tmp += 1;
            }
        }
    }
    return tmp;
}

var cnt = 0; // 총 블록 수
var res = new Array();
for(let x = 0; x < n; x++){
    for(let y = 0; y < n; y++){
        if(visited[x][y] === 0 && graph[x][y] === 1){
            cnt++;
            res.push(bfs(x, y));
        }
    }
}

console.log(cnt);
res.sort((a, b) => a - b);
res.forEach((e) => {
    console.log(e)
})