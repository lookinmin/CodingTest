var uniquePathsWithObstacles = function(grid) {
    var n = grid.length;
    var m = grid[0].length;
    var dp = Array.from(Array(n), () => Array(m).fill(0));

    if(grid[0][0] === 1){
        return 0;
    }

    dp[0][0] = 1;

    for (let i = 1; i < n; i++) {
        dp[i][0] = grid[i][0] === 1 ? 0 : dp[i-1][0];
    }
    for (let j = 1; j < m; j++) {
        dp[0][j] = grid[0][j] === 1 ? 0 : dp[0][j-1];
    }

    for(let x = 1; x < n; x++){
        for(let y = 1; y < m; y++){
            if(grid[x][y] === 0){
                dp[x][y] = dp[x-1][y] + dp[x][y-1];
            }
        }
    };

    return dp[n-1][m-1];
};