/**
 * @param {number} candies
 * @param {number} num_people
 * @return {number[]}
 */
var distributeCandies = function (candies, num_people) {
  var res = new Array(num_people).fill(0);

  let give = 1;
  let idx = 0;

  while (candies > 0) {
    res[idx % num_people] += Math.min(give, candies);
    candies -= give;
    give++;
    idx++;
  }

  return res;
};
