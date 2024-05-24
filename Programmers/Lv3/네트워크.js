function solution(n, computers) {
    var answer = 0;
    var graph = Array.from(Array(n), () => Array())
    
    for(let i=0;i<n;i++){
        for(let j = 0; j<n;j++){
            if(i !== j){
                if(computers[i][j] == 1){
                    graph[i].push(j)
                }
            }
        }
    }
    
    var visited = new Set();
    const bfs = (s) => {
        var q = [s]
        visited.add(s)
        
        while(q.length > 0){
            var node = q.shift();
            
            graph[node].forEach(v => {
                if(!visited.has(v)){
                    visited.add(v)
                    q.push(v)
                }
            })
        }
    }
    
    for(let v = 0; v < n; v++){
        if(!visited.has(v)){
            bfs(v);
            answer += 1;
        }
    }
    
    return answer;
}