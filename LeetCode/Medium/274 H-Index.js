/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function (citations) {
  citations.sort((a, b) => a - b);
  const k = citations.length;
  for (let i = 0; i < k; i++) {
    let sub = k - i;
    if (citations[i] >= sub) {
      return sub;
    }
  }
  return 0;
};
