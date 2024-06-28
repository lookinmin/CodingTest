var input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
var n = Number(input[0]);
var lst = input[1].split(' ').map(Number);

var dp = new Array(n).fill(1);

for(let i = 0;i < n;i++){
    for(let j = 0; j < i;j++){
        if(lst[i] > lst[j]){
            dp[i] = Math.max(dp[i], dp[j] + 1);
        }
    }
}

console.log(Math.max(...dp))