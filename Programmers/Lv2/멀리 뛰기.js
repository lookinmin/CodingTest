function solution(n) {
    var answer = 0;
    var dp = Array(n + 1).fill(0);
    dp[1] = 1
    dp[2] = 2
    
    if(n < 3){
        return n;
    }
    
    for(let i = 3; i < (n + 1); i++){
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
    }
    
    return dp[n];
}