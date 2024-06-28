var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var [n, k] = input[0].split(' ').map(Number);
var lst = input[1].split(' ').map(Number);
input.splice(0, 2)

var psum = new Array(n + 1).fill(0);

for(let i = 1; i<n+1;i++){
    psum[i] = psum[i - 1] + lst[i - 1];
}

for(let i = 0;i < k;i++){
    var [a, b] = input[i].split(' ').map(Number);
    a -= 1;
    b -= 1;
    var len = b - a + 1;
    var sum = psum[b + 1] - psum[a]
    console.log((sum / len).toFixed(2))
}