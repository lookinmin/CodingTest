/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function (num, k) {
  let res = [];
  let i = num.length - 1;

  while (i >= 0 || k > 0) {
    if (i >= 0) {
      k += num[i]; // 각 자리의 수와 k의 일의 자리 합산
      i--;
    }
    res.unshift(k % 10); // 일의 자리수 추가
    k = Math.floor(k / 10); // k를 다음 자리로 이동
  }

  return res;
};
