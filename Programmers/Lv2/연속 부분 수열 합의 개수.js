function solution(elements) {
  var tmp = new Set();

  const k = elements.length;
  var cvt = elements.concat(elements);

  for (let len = 1; len <= k; len++) {
    for (let idx = 0; idx < k; idx++) {
      let sumArr = cvt.slice(idx, idx + len).reduce((a, b) => a + b, 0);
      tmp.add(sumArr);
    }
  }

  return tmp.size;
}
