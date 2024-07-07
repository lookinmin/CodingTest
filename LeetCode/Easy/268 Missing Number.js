/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    var k = nums.length;
    var origin = new Array(k + 1);
    for(let i = 0; i <= k; i++){
        origin[i] = i;
    }
    var sortedNums = nums.sort((a, b) => a - b);
    
    for(let idx = 0; idx < k; idx++){
        if (origin[idx] !== sortedNums[idx]){
            return origin[idx];
        }
    }
    return origin[origin.length - 1];
};