const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');
const n = parseInt(input[0]);
input.splice(0, 1);

const students = new Set();

const gcd = (a, b) => {
  while (b !== 0) {
    const tmp = b;
    b = a % b;
    a = tmp;
  }
  return Math.abs(a);
};

const normalize = (a, b) => {
  const mod = gcd(a, b);
  a /= mod;
  b /= mod;
  // 음수 방향을 다르게 보도록 정규화
  return `${a},${b}`;
};

for (let i = 0; i < n; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  students.add(normalize(a, b));
}

console.log(students.size);
