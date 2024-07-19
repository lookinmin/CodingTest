var solve = function(board) {
    if(board.length === 0){
        return null;
    }
    var n = board.length;
    var m = board[0].length;

    var dx = [-1, 1, 0, 0];
    var dy = [0, 0, -1, 1];

    const dfs = (x, y) => {
        if(x < 0 || y < 0 || x >= n || y >= m || board[x][y] === 'X' || board[x][y] === 'W'){
            return
        }
        board[x][y] = 'W';

        for(let i = 0; i < 4; i++){
            let nx = x + dx[i];
            let ny = y + dy[i];
            dfs(nx, ny);
        }
        return
    }

    for(let i = 0; i < n; i++){
        for(let j = 0; j < m; j++){
            if(board[i][j] === 'O' && (i === 0 || i === n-1 || j === 0 || j === m-1)){
                // borderLine에 위치
                dfs(i, j);
            }
        }
    }

    for(let i = 0; i < n; i++){
        for(let j = 0; j < m; j++){
            if(board[i][j] === 'W'){
                board[i][j] = 'O';
            } else {
                board[i][j] = 'X';
            }
        }
    }

    return board;
};