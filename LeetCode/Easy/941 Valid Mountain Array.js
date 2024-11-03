/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function (arr) {
  let flag = true;
  // upside

  if (arr.length < 3) {
    return false;
  }

  for (let i = 1; i < arr.length; i++) {
    if (flag && arr[i] > arr[i - 1]) {
      continue;
    }
    if (flag && i > 1 && arr[i] < arr[i - 1]) {
      flag = false;
      continue;
    }
    if (!flag && arr[i] < arr[i - 1]) {
      continue;
    } else {
      return false;
    }
  }
  if (flag) {
    return false;
  } else {
    return true;
  }
};
