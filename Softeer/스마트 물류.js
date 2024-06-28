var input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
var [n, k] = input[0].split(' ').map(Number);
var lst = input[1].split('');
visited = new Array(n).fill(0);

var res = 0;
for(let i = 0; i < n; i++){
    if(lst[i] === 'P'){
        for(let j = i-k;j<i+k+1;j++){
            if(0<=j && j < n){
                if(lst[j] === 'H' && visited[j] === 0){
                    visited[j] = 1;
                    res += 1;
                    break;
                }
            }
        }
    }
}
console.log(res)