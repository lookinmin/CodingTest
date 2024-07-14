/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if(nums.length === 0) return 0;

    var k = 0;
    var cnt = 0;
    for(let i = 0; i < nums.length; i++){
        if(i === nums.length - 1 || nums[i] != nums[i + 1]){
            nums[k++] = nums[i];
            cnt = 0;
        } else {
            if(cnt < 1){
                nums[k++] = nums[i];
                cnt++;
            } else {
                cnt++;
            }
        }
    }
    return k;
};
