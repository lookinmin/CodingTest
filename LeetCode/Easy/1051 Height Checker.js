/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function (heights) {
  prev = [...heights];
  heights.sort((a, b) => a - b);
  let cnt = 0;
  for (let i = 0; i < heights.length; i++) {
    if (prev[i] !== heights[i]) cnt++;
  }
  return cnt;
};
