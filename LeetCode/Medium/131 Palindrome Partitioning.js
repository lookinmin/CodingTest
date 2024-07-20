/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    var res = new Array();
    const dfs = (start, path) => {
        if (start === s.length) {
            res.push([...path]);
            return;
        }

        for(let end = start; end < s.length; end++){
            if(isPalindrome(start, end)){
                path.push(s.slice(start, end + 1));
                dfs(end + 1, path);
                path.pop();
            }
        }
    };

    const isPalindrome = (start, end) => {
        while(start < end){
            if(s[start++] !== s[end--]) return false;
        }
        return true;
    };

    dfs(0, []);
    return res;
    
};