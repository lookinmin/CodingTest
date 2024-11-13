#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// dfs
int dfs(int hp, vector<vector<int>>& dungeons, vector<int>& visited, int cnt){
    if (hp <= 0 || find(visited.begin(), visited.end(), 0) == visited.end()) {
        return cnt;
    }
    
    int maxCnt = cnt;
    
    for(int i = 0; i < visited.size(); i++){
        if(visited[i] == 0 && hp >= dungeons[i][0]){
            visited[i] = 1;
            maxCnt = max(maxCnt, dfs(hp - dungeons[i][1], dungeons, visited, cnt + 1));
            visited[i] = 0;
        }
    }
    
    return maxCnt;
}

int solution(int k, vector<vector<int>> dungeons) {
    int n = dungeons.size();
    vector<int> visited(n, 0);
    
    int answer = dfs(k, dungeons, visited, 0);
    return answer;
}