var subsets = function(nums) {
    var res = new Set();
    res.add([]);
    var k = nums.length;

    const dfs = (len, outs, idx) => {
        if(outs.length === len){
            res.add([...outs]);
        }
        for(let i = idx; i < k; i++){
            if(visited[i] === 0){
                outs.push(nums[i]);
                visited[i] = 1;
                dfs(len, outs, i + 1);
                visited[i] = 0;
                outs.pop();
            }
        }
    }

    for(let i = 1; i <= k; i++){
        var visited = Array(k).fill(0);
        dfs(i, [], 0);
    }

    res = Array.from(res);
    return res;
};