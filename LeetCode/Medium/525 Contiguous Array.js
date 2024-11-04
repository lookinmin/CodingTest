/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function (nums) {
  const n = nums.length;
  let psum = Array(n + 1).fill([0, 0]);
  psum[0] = [0, 0];
  // count 0, count 1

  for (let i = 1; i < n + 1; i++) {
    if (nums[i - 1] === 0) {
      psum[i] = [psum[i - 1][0] + 1, psum[i - 1][1]];
    } else {
      psum[i] = [psum[i - 1][0], psum[i - 1][1] + 1];
    }
  }

  let idxMap = new Map();
  idxMap.set(0, 0);
  let res = 0;
  for (let idx = 1; idx < n + 1; idx++) {
    const diff = psum[idx][0] - psum[idx][1];

    if (idxMap.has(diff)) {
      res = Math.max(res, idx - idxMap.get(diff));
    } else {
      idxMap.set(diff, idx);
    }
  }

  return res;
};

// ---------------------------------------------------------

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function (nums) {
  const n = nums.length;
  let res = 0;

  let cntMap = new Map();
  cntMap.set(0, -1);

  let cnt = 0;
  for (let i = 0; i < n; i++) {
    cnt += nums[i] === 1 ? 1 : -1;

    if (cntMap.has(cnt)) {
      res = Math.max(res, i - cntMap.get(cnt));
    } else {
      cntMap.set(cnt, i);
    }
  }

  return res;
};
