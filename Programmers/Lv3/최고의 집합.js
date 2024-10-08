function solution(n, s) {
  if (s / n < 1) {
    return [-1];
  }

  const baseValue = Math.floor(s / n);
  // 기본값
  const res = new Array(n).fill(baseValue);

  let mod = s % n;
  // 나머지, +1 씩 해준다.
  for (let i = n - 1; i >= 0 && mod > 0; i--) {
    // 오름차순이니까 뒤에서부터
    res[i]++;
    mod--;
  }
  return res;
}
