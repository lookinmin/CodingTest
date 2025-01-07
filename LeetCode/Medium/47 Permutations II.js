/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function (nums) {
  const n = nums.length;
  let res = [];
  let visited = Array(n).fill(false);

  nums.sort((a, b) => a - b);

  const dfs = (out) => {
    if (out.length === n) {
      res.push([...out]);
      return;
    }

    for (let i = 0; i < n; i++) {
      if (visited[i]) continue;

      if (i > 0 && nums[i] === nums[i - 1] && !visited[i - 1]) continue;
      // 현재 수와 이전 수가 같음(1, 1) and 이전 수가 사용되지 않았음 -> pass

      visited[i] = true;
      out.push(nums[i]);
      dfs(out);

      out.pop();
      visited[i] = false;
    }
  };
  dfs([]);
  return res;
};
