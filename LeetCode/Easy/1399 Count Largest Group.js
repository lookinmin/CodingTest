/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function (n) {
  const digitSum = (num) => {
    let sum = 0;
    while (num > 0) {
      sum += num % 10;
      num = Math.floor(num / 10);
    }
    return sum;
  };

  const groups = new Map();

  for (let i = 1; i <= n; i++) {
    const sum = digitSum(i);
    groups.set(sum, (groups.get(sum) || 0) + 1);
  }

  let maxSize = -1;
  for (let size of groups.values()) {
    maxSize = Math.max(maxSize, size);
  }

  let cnt = 0;
  for (let size of groups.values()) {
    if (size === maxSize) cnt++;
  }
  return cnt;
};
