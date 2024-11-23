/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function (arr) {
  let counter = new Map();
  for (let num of arr) {
    counter.set(num, (counter.get(num) || 0) + 1);
  }
  const k = arr.length;
  for (let [key, value] of counter) {
    if (value > k * 0.25) {
      return key;
    }
  }
};
