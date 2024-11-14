#include <bits/stdc++.h>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    // 시작은 1번
    unordered_map<int, vector<int>> graph;
    for(auto& e : edge){
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }
    
    queue<int> q;
    vector<int> visited(n + 1, 0);
    
    q.push(1);
    visited[1] = 1;
    
    while(!q.empty()){
        int node = q.front();
        q.pop();
        
        for(int& adj : graph[node]){
            if(visited[adj] == 0){
                q.push(adj);
                visited[adj] = visited[node] + 1;
            }
        }
    }
    
    vector<int> sliced(visited.begin() + 1, visited.end());
    
    int maxVal = *max_element(sliced.begin(), sliced.end());
    
    int cnt = count(sliced.begin(), sliced.end(), maxVal);
    
    return cnt;
}