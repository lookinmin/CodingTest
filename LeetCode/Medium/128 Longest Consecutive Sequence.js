/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    // sort()는 O(n log n)
    if(nums.length === 0){
        return 0;
    }

    let numSet = new Set(nums);
    let res = 0;

    for(let num of numSet){
        if(!numSet.has(num - 1)){
            // 현재 숫자가 가장 작은 수
            let cur = num;
            let seq = 1;

            while(numSet.has(cur + 1)){
                cur++;
                seq++;
            }
            res = Math.max(res, seq);
        }
    }

    return res;
};