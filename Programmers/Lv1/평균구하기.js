function solution(arr) {
  var sum = arr.reduce((prev, nxt) => {
    return prev + nxt;
  }, 0);
  return sum / arr.length;
}
