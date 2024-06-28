var fs = require('fs')
var input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
var n = Number(input[0])

var res = ""
for(let i = 1;i < n + 1; i++){
    var [s, t] = input[i].split(" ");
    s = s.toUpperCase();
    idx = -1
    for(let i = 0; i < s.length; i++){
        if(s[i] == 'X'){
            idx = i;
            break;
        }
    }
    res += t[idx];
}

console.log(res.toUpperCase());