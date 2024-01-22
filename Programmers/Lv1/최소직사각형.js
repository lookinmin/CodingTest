function solution(sizes) {
  for (size of sizes) {
    size.sort((a, b) => b - a);
  }
  var maxW = sizes.reduce((max, item) => (item[0] > max ? item[0] : max), 0);
  var maxH = sizes.reduce((max, item) => (item[1] > max ? item[1] : max), 0);
  return maxW * maxH;
}
