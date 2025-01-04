/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers = function (matrix) {
  let minRows = [];
  for (let i = 0; i < matrix.length; i++) {
    minRows.push(Math.min(...matrix[i]));
  }

  let maxCols = [];
  for (let i = 0; i < matrix[0].length; i++) {
    let maxNum = -1;
    for (let j = 0; j < matrix.length; j++) {
      maxNum = Math.max(maxNum, matrix[j][i]);
    }
    maxCols.push(maxNum);
  }
  const set1 = new Set(minRows);
  var res = maxCols.filter((val) => set1.has(val));
  return res;
};
