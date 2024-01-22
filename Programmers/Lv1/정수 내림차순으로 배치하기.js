function solution(n) {
  var answer = 0;
  var arr = [];
  while (n > 0) {
    arr.push(n % 10);
    n = Math.floor(n / 10);
  }
  arr.sort((a, b) => a - b);
  for (let i = 0; i < arr.length; i++) {
    answer += arr[i] * 10 ** i;
  }
  return answer;
}
