const input = require('fs').readFileSync('/dev/stdin').toString().trim();
var postfix = '';
var stack = [];

const op = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0};

for(w of input){
    if(w >= 'A' && w <= 'Z'){
        postfix += w;
    } else if (w === '('){
        stack.push(w)
    } else if (w == ')'){
        while(stack.length > 0 && stack.at(-1) !== '('){
            postfix += stack.pop();
        }
        stack.pop()
    } else {
        while(stack.length > 0 && op[w] <= op[stack.at(-1)]){
            postfix += stack.pop();
        }
        stack.push(w)
    }
}

while(stack.length > 0){
    postfix += stack.pop();
}

console.log(postfix)