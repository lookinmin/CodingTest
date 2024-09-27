/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function (people) {
  people.sort((a, b) => b[0] - a[0] || a[1] - b[1]);

  let res = [];
  for (let [h, k] of people) {
    res.splice(k, 0, [h, k]);
  }

  return res;
};
