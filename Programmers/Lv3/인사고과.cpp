#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> scores) {
    pair<int, int> wanho = make_pair(scores[0][0], scores[0][1]);
    
    sort(scores.begin(), scores.end(), [](const vector<int>& a, const vector<int>& b){
        if(a[0] != b[0]){
            return a[0] > b[0];
        }
        return a[1] < b[1];
    });
    
    int maxB = 0;
    int rank = 1;
    for(auto& score : scores){
        if(score[0] > wanho.first && score[1] > wanho.second){
            return -1;
        }
        
        if(score[1] >= maxB){
            maxB = score[1];
            if((score[0] + score[1]) > (wanho.first + wanho.second)){
                rank++;
            }
        }
    }
    return rank;
}