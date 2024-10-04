const check = (num) => {
  if (num < 5 && num != 2) return true;
  if ((num - 2) % 5 === 0) return false;

  return check(Math.floor(num / 5));
};

function solution(n, l, r) {
  var res = 0;
  for (let idx = l - 1; idx < r; idx++) {
    if (check(idx)) {
      res++;
    }
  }
  return res;
}
