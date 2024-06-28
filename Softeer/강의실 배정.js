const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = parseInt(input[0]);
const lectures = [];

for (let i = 1; i <= n; i++) {
    const [s, f] = input[i].split(' ').map(Number);
    lectures.push([s, f]);
}

lectures.sort((a, b) => a[1] - b[1]);

let cnt = 1;
let last = lectures[0][1];

for (let i = 1; i < lectures.length; i++) {
    const now = lectures[i];
    if (last <= now[0]) {
        cnt += 1;
        last = now[1];
    }
}
console.log(cnt);