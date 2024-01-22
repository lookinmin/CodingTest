function solution(arr, divisor) {
  arr.sort((a, b) => a - b);
  var tmp = arr.filter((value) => value % divisor == 0);
  if (tmp.length > 0) {
    return tmp;
  } else {
    return [-1];
  }
}
