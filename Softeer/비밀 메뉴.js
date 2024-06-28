var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var [n, m, k] = input[0].split(' ').map(Number)
key = new Array();
key = input[1].split(' ').map(Number)
lst = new Array();
lst = input[2].split(' ').map(Number)

if(lst.length < key.length){
    console.log("normal")
    process.exit();
}

var k = key.length;

for(let i = 0; i < lst.length - k + 1;i++){
    var tmp = lst.slice(i, i + k);
    var stand = JSON.stringify(key);
    if(stand === JSON.stringify(tmp)){
        console.log('secret');
        process.exit();
    }
}
console.log("normal")