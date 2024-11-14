#include <bits/stdc++.h>

class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int minVal = numeric_limits<int>::max();

        vector<vector<int>> res;
        for(int i = 0; i < arr.size() - 1; i++){
            int a = arr[i];
            int b = arr[i + 1];
            if(abs(b-a) < minVal){
                res.clear();
                minVal = abs(b - a);
                res.push_back({a, b});
            } else if(abs(b - a) == minVal){
                res.push_back({a, b});
            }
        }
        return res;
    }
};