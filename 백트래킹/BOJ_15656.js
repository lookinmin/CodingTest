const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
let [n, m] = input[0].split(' ').map(Number)
let arr = input[1].split(' ').map(Number).sort((a, b) => a - b);

var res = [];
var answer = [];
const dfs = (depth) => {
    if(depth === m){
        answer.push(res.join(' ') + '\n');
        return
    }
    
    for(num of arr){
        res.push(num);
        dfs(depth + 1);
        res.pop();
    }
}

dfs(0);
console.log(answer.join(''));