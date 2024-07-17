var numDecodings = function(s) {
    if(s[0] === '0'){
        return 0;
    }
    
    const k = s.length;
    const dp = new Array(k + 1).fill(0);

    dp[0] = dp[1] = 1;

    for(let i = 2; i <= k; i++){
        var one = parseInt(s[i - 1]);
        var two = parseInt(s.substring(i - 2, i));

        if(1<=one && one <= 9){
            dp[i] += dp[i - 1];
        }
        if(10<=two && two<=26){
            dp[i] += dp[i - 2];
        }
    }

    return dp[k];
};