/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    var tmp = new Array();
    var cnt = 0;
    for(let i = 0; i < nums.length; i++){
        if(nums[i] !== 0){
            tmp.push(nums[i]);
        } else {
            cnt++;
        }
    }

    for(let i = 0; i < cnt; i++){
        tmp.push(0);
    }

    for(let idx = 0; idx < nums.length; idx++){
        nums[idx] = tmp[idx];
    }
};