/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums = nums.sort((a, b) => (a - b));
    var res = new Set();
    res.add([]);
    const dfs = (len, outs, idx) => {
        if(outs.length === len){
            res.add([...outs]);
        }
        for(let i = idx; i < nums.length; i++){
            if(i > idx && nums[i] === nums[i - 1]) continue;
            outs.push(nums[i]);
            dfs(len, outs, i + 1);
            outs.pop();
        }
    }

    for(let k = 1; k < nums.length + 1; k++){
        dfs(k, [], 0);
    }
    return [...res];
};
