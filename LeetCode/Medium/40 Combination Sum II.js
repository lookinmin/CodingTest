var combinationSum2 = function(candidates, target) {
    var k = candidates.length;
    candidates = candidates.sort((a, b) => a - b);
    var visited = new Array(k).fill(0);

    var res = new Array();
    const dfs = (outs, idx) => {
        let tmp = outs.reduce((a, b) => a + b, 0);
        if(tmp === target){
            res.push([...outs]);
        }
        if(tmp > target){
            return;
        }

        for(let i = idx; i < k; i++){
            if (i > 0 && candidates[i] === candidates[i - 1] && !visited[i - 1])
                continue;
            if(visited[i] === 0){
                visited[i] = 1;
                outs.push(candidates[i]);
                dfs(outs, i + 1);
                outs.pop();
                visited[i] = 0;
            }
        }
    }

    dfs([], 0);
    return res;
};