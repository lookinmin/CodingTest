var dominantIndex = function (nums) {
  let tmp = [];
  for (let idx = 0; idx < nums.length; idx++) {
    tmp.push([nums[idx], idx]);
  }
  tmp.sort((a, b) => b[0] - a[0]);
  let a = tmp[0][0];
  let b = tmp[1][0];
  return a >= b * 2 ? tmp[0][1] : -1;
};
