var fs = require('fs');
var [n,...arr] = fs.readFileSync('/dev/stdin').toString().trim().split(/\s/);
n = Number(n);
arr = arr.map(Number);

var maxVal = -1;
for(let i = 2; i<=Math.max(...arr);i++){
    cnt = 0;
    arr.forEach((e) => {
        if(e % i === 0){
            cnt++;
        }
    })
    maxVal = Math.max(maxVal, cnt)
}

console.log(maxVal)