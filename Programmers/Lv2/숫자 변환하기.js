function solution(x, y, n) {
  var answer = 0;
  var tmp = new Set();

  tmp.add(x);
  var cnt = 0;
  while (tmp.size > 0) {
    if (tmp.has(y)) {
      return cnt;
    }
    var nxt = new Set();
    for (let value of tmp) {
      if (value + n <= y) {
        nxt.add(value + n);
      }
      if (value * 2 <= y) {
        nxt.add(value * 2);
      }
      if (value * 3 <= y) {
        nxt.add(value * 3);
      }
    }
    cnt++;

    tmp = nxt;
  }
  return -1;
}
