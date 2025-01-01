/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function (arr) {
  var res = -1;
  var tmp = new Map();
  for (let i = 0; i < arr.length; i++) {
    tmp.set(arr[i], (tmp.get(arr[i]) || 0) + 1);
  }
  for (const [key, value] of tmp) {
    if (key === value) {
      res = Math.max(res, key);
    }
  }
  return res;
};
