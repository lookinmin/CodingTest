var maxIncreaseKeepingSkyline = function(grid) {
    var west = new Array();
    var north = new Array();
    const n = grid.length;

    for(let i = 0; i < n; i++){
        var wtmp = 0;
        var htmp = 0;
        for(let j = 0; j < n; j++){
            wtmp = Math.max(wtmp, grid[i][j]);
            htmp = Math.max(htmp, grid[j][i]);
        }
        west.push(wtmp);
        north.push(htmp);
    }

    var newGrid = Array.from(Array(n), () => Array(n).fill(0));

    for(let i = 0; i < n; i++){
        for(let j = 0; j < n; j++){
            newGrid[i][j] = Math.min(west[i], north[j]);
        }
    }
    var res = 0;
    for(let x = 0; x < n; x++){
        for(let y = 0; y < n; y++){
            res += (newGrid[x][y] - grid[x][y]);
        }
    }
    return res;
};