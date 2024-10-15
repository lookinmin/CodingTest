/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function (nums, target) {
  var memo = new Map();

  const dfs = (remain) => {
    if (remain === 0) {
      return 1;
    }
    if (memo.has(remain)) {
      return memo.get(remain);
    }

    let total = 0;
    for (let num of nums) {
      if (remain - num >= 0) {
        total += dfs(remain - num);
      }
    }

    memo.set(remain, total);
    return total;
  };

  return dfs(target);
};
