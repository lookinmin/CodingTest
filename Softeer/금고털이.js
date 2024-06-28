var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var [w, n] = input[0].split(' ').map(Number);
var arr = new Array();

for(let i = 1; i < n + 1; i++){
    var [weight, valuePerWeight] = input[i].split(' ').map(Number);
    arr.push([weight, valuePerWeight]);
}

arr.sort((a, b) => b[1] - a[1])
var res = 0;

for(let i = 0; i < arr.length; i++){
    if(arr[i][0] <= w){
        res += (arr[i][0] * arr[i][1]);
        w -= arr[i][0];
    }else{
        res += (w * arr[i][1]);
        break
    }
}
console.log(res)