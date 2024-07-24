var numIslands = function(grid) {
    var dx = [-1, 1, 0, 0];
    var dy = [0, 0, -1, 1];

    const n = grid.length;
    const m = grid[0].length;

    var visited = Array.from(Array(n), () => Array(m).fill(0));
    var res = 0;
    const bfs = (a, b) => {
        var q = [];
        q.push([a, b]);
        visited[a][b] = 1;

        while(q.length > 0){
            let [x, y] = q.shift();

            for(let i = 0; i < 4; i++){
                let nx = x + dx[i];
                let ny = y + dy[i];

                if(0<=nx && nx < n && 0<=ny && ny < m && visited[nx][ny] === 0 && grid[nx][ny] === '1'){
                    q.push([nx, ny]);
                    visited[nx][ny] = 1;
                }
            }
        }
        return;
    }

    for(let x = 0; x < n; x++){
        for(let y = 0; y < m; y++){
            if(grid[x][y] === '1' && visited[x][y] === 0){
                bfs(x, y);
                res++;
            }
        }
    }

    return res;
};