var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var [n, m] = input[0].split(' ').map(Number);

var drive = new Array(100).fill(0);
var test = new Array(100).fill(0);

// Correcting the input array to remove the first line with `n` and `m`
input.splice(0, 1);

var dIndex = 0;
for (let i = 0; i < n; i++) {
    var [num, velo] = input[i].split(' ').map(Number);
    var tmp = new Array(num).fill(velo);
    drive.splice(dIndex, num, ...tmp);   
    dIndex += num;
}

input.splice(0, n);
var tIndex = 0;
for (let j = 0; j < m; j++) {
    var [num, velo] = input[j].split(' ').map(Number);
    var tmp = new Array(num).fill(velo);
    test.splice(tIndex, num, ...tmp);   
    tIndex += num;
}

var maxVal = 0;
for (let i = 0; i < 100; i++) {
    maxVal = Math.max(maxVal, test[i] - drive[i]);
}

console.log(maxVal);
