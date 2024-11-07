const MOD = 10 ** 9 + 7;
const isPrime = (num) => {
  let s = Math.sqrt(num);

  for (let i = 2; i <= s; i++) {
    if (num % i === 0) return false;
  }

  return num > 1;
};

var numPrimeArrangements = function (n) {
  let a = 0; // 소수의 갯수
  let b = 0; // 비소수의 갯수
  let res = 1;

  for (let i = 1; i <= n; i++) {
    res *= isPrime(i) ? ++a : ++b;
    res = res % MOD;
  }

  return res;
};
