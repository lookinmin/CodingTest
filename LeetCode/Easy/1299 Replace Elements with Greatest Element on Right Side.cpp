#include<bits/stdc++.h>
class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n = arr.size();
        if(n == 1){
            return {-1};
        }

        int maxRight = -1;

        for(int i = n - 1; i >= 0; i--){
            int cur = arr[i];
            arr[i] = maxRight;
            maxRight = max(maxRight, cur);
        }
        return arr;
    }
};