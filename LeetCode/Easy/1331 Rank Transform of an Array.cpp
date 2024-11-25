#include <bits/stdc++.h>
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        int rank = 0;
        int n = arr.size();
        vector<int> res(n, 0);
        priority_queue<vector<int>> heap;
        for(int i = 0; i < n; i++){
            heap.push({-arr[i], i});
        }
        int prev = 1e9 + 7;
        while(!heap.empty()){
            auto v = heap.top();
            int val = v[0]*-1;
            int idx = v[1];
            heap.pop();
            val *= -1;
            if(val != prev){
                rank++;
                res[idx] = rank;
                prev = val;
            } else {
                res[idx] = rank;
            }
        }

        return res;
    }
};