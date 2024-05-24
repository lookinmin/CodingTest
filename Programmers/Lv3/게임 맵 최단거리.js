function solution(maps) {
    var answer = 0;
    const n = maps.length;
    const m = maps[0].length;
    
    var visited = Array.from(Array(n), () => Array(m).fill(0))
    const dx = [-1, 1, 0, 0]
    const dy = [0, 0, -1, 1]
    
    
    const bfs = () => {
        let q = [[0, 0, 1]]
        visited[0][0] = 1;
        
        while(q.length > 0){
            const [x, y, cnt] = q.shift();
            
            if(x==n-1 && y==m-1){
                return cnt;
            }
            
            for(let i=0;i<4;i++){
                var nx = x + dx[i];
                var ny = y + dy[i];
                
                if(0<=nx && nx < n && 0<=ny && ny<m && visited[nx][ny] == 0 && maps[nx][ny] == 1){
                    q.push([nx,ny,cnt + 1])
                    visited[nx][ny] = 1
                }
            }
        }
        return -1;
    }
    
    return bfs();
}