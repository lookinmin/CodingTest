var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var [n, m, k] = input[0].split(' ').map(Number);
var lst1 = input[1].split(' ').map(Number);  // 길이는 n
var lst2 = input[2].split(' ').map(Number);  // 길이는 m

var dp = Array.from(Array(n + 1), () => Array(m + 1).fill(0));
var res = 0;

for(let i = 1; i < n + 1;i++){
    for(let j = 1;j < m + 1;j++){
        if(lst1[i-1] === lst2[j-1]){
            dp[i][j] = dp[i-1][j-1] + 1;
            res = Math.max(res, dp[i][j]);
        }
    }
}

console.log(res)