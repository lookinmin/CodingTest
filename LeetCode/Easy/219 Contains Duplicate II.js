// forEach((value, idx) => {...}) 은 중간에 break 시킬 수 없다.

var containsNearbyDuplicate = function(nums, k) {
    var tmp = new Map();
    for (let idx = 0; idx < nums.length; idx++) {
        let num = nums[idx];
        if (tmp.has(num) && (idx - tmp.get(num) <= k)) {
            return true;
        }
        tmp.set(num, idx);
    }
    return false;
};
