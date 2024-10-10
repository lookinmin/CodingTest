function solution(scores) {
  var me = scores[0];
  scores = scores.sort((a, b) => b[0] - a[0] || a[1] - b[1]);
  let maxB = 0;
  var cnt = 1;
  for (let [a, b] of scores) {
    if (a > me[0] && b > me[1]) {
      return -1;
    }

    if (b >= maxB) {
      maxB = b;
      if (a + b > me[0] + me[1]) {
        cnt++;
      }
    }
  }

  return cnt;
}
