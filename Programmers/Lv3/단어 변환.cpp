#include <bits/stdc++.h>

using namespace std;

int solution(string begin, string target, vector<string> words) {
    int n = begin.length();
    set<string> visited;
    queue<pair<string, int>> q;
    
    visited.insert(begin);
    q.push({begin, 0});
    
    while(!q.empty()){
        auto tmp = q.front();
        string node = tmp.first;
        int cnt = tmp.second;
        
        q.pop();
        
        if(node == target){
            return cnt;
        }
        
        for(string& word : words){
            if(visited.find(word) == visited.end()){
                int diff = 0;
            
                for(int i = 0; i < n; i++){
                    if(node[i] != word[i]){
                        diff++;
                    }
                }
                if(diff == 1){
                    q.push({word, cnt + 1});
                    visited.insert(word);
                }   
            }
        }

    }
    return 0;
}