// O(n * m)
var nextGreaterElement = function (nums1, nums2) {
  var res = [];
  for (let num of nums1) {
    let idx = nums2.indexOf(num);
    var flag = false;
    for (let i = idx + 1; i < nums2.length; i++) {
      if (nums2[i] > num) {
        res.push(nums2[i]);
        flag = true;
        break;
      }
    }
    if (!flag) res.push(-1);
  }

  return res;
};

// O(n + m)

var nextGreaterElement = function (nums1, nums2) {
  var nxt = new Map();
  var stack = [];
  for (let num of nums2) {
    while (stack.length > 0 && stack[stack.length - 1] < num) {
      nxt.set(stack.pop(), num);
      // 마지막 값보다 현재 탐색중인 값이 크다면
    }
    stack.push(num);
  }

  while (stack.length > 0) {
    nxt.set(stack.pop(), -1);
  }

  var res = [];
  for (let num of nums1) {
    res.push(nxt.get(num));
  }
  return res;
};
