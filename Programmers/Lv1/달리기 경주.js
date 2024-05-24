function solution(players, callings) {
    var rank = {};
    cnt = 0
    for(name of players){
        rank[name] = cnt;
        cnt += 1;
    }
    
    for(call of callings){
        let idx = rank[call];
        let front = players[idx - 1];
        // 한 칸 앞에
        
        players[idx - 1] = call;
        players[idx] = front
        
        rank[call] = idx - 1;
        rank[front] = idx;
    }
    return players;
}