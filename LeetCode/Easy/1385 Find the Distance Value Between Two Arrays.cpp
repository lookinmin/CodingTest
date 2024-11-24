#include <bits/stdc++.h>

class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        int cnt = 0;
        sort(arr1.begin(), arr1.end());
        sort(arr2.begin(), arr2.end());

        for(int& x : arr1){
            bool flag = true;
            for(int& y : arr2){
                if(abs(x-y) > d){
                    continue;
                } else {
                    flag = false;
                    break;
                }
            }
            if(flag) cnt++;
        }
        return cnt;
    }
};