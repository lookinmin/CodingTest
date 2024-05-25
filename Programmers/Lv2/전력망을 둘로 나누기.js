function solution(n, wires) {
    var answer = 1e9;
    
    var graph = Array.from(Array(n + 1), () => Array());
    for(wire of wires){
        let a = wire[0];
        let b = wire[1];
        
        graph[a].push(b)
        graph[b].push(a)
    }
    
    const bfs = (start, cant) => {
        var q = [start];
        var visited = new Set();
        visited.add(start)
        
        var cnt = 1;
        
        while(q.length > 0){
            var node = q.shift();
            
            graph[node].forEach(v => {
                if(v !== cant){
                    if(!visited.has(v)){
                        q.push(v);
                        visited.add(v)
                        cnt++;
                    }
                }
                
            })
        }
        
        return cnt;
    }
    
    for(let v = 1; v < n + 1; v++){
        graph[v].forEach(e => {
            var a = bfs(e, v);
            var b = bfs(v, e);
            answer = Math.min(answer, Math.abs(a-b));
        })
    }
    
    
    return answer;
}