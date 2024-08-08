/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  var res = nums1.filter((x) => nums2.includes(x));
  res = new Set(res);
  return [...res];
};
