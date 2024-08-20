/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function (k, n) {
  var res = [];

  const dfs = (start, out, sum) => {
    // 길이가 k이고 합이 n인 경우 결과에 추가
    if (out.length === k && sum === n) {
      res.push([...out]);
      return;
    }

    // 길이가 k보다 크거나 합이 n보다 크면 탐색 중단
    if (out.length > k || sum > n) {
      return;
    }

    for (let num = start; num <= 9; num++) {
      out.push(num);
      dfs(num + 1, out, sum + num);
      out.pop();
    }
  };

  dfs(1, [], 0);
  return res;
};
