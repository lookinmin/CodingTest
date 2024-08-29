/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function (nums) {
  const countMap = new Map();
  let res = 0;

  for (let num of nums) {
    countMap.set(num, (countMap.get(num) || 0) + 1);
  }
  // 값 : 몇개

  for (let [key, value] of countMap) {
    if (countMap.has(key + 1)) {
      // +1 차이
      res = Math.max(res, value + countMap.get(key + 1));
    }
  }

  return res;
};
