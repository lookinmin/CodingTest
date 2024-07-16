/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    var res = new Array();
    const dfs = (idx = 1, outs = []) => {
        if(outs.length === k){
            res.push([...outs]);
            return;
        }

        for(let i = idx; i <= n; i++){
            outs.push(i);
            dfs(i + 1, outs);
            outs.pop();
        }
    }

    dfs();
    return res;
};