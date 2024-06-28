var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var [n, m, k] = input[0].split(' ').map(Number)
var lst = input[1].split(' ').map(Number)
var visited = new Array(n).fill(0);

var out = [];
const dfs = (depth) => {
    if(depth === n){
        calculate(out);
        return;
    }
    for(let i = 0; i < n; i++){
        if(visited[i] === 0){
            out.push(lst[i])
            visited[i] = 1
            dfs(depth + 1)
            visited[i] = 0
            out.pop()
        }
    }
}

var res = Infinity;

const calculate = (arr) => {
    let seq = [...arr];
    let idx = 0;

    let work = k;
    let bucket = 0;
    let total = 0;

    while(work > 0){
        if(bucket + seq[idx] <= m){
            bucket += seq[idx];
            idx += 1;
            if(idx === seq.length) idx = 0;
        } else {
            total += bucket;
            bucket = 0;
            work -= 1;
        }
    }
    res = Math.min(res, total);
}

dfs(0)

console.log(res)
