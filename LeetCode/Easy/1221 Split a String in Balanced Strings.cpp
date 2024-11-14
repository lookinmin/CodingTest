#include <bits/stdc++.h>
class Solution {
public:
    int balancedStringSplit(string s) {
        int R = 0, L = 0, max = 0;
        for(char& c : s){
            if(c == 'R'){
                R++;
            } else {
                L++;
            }
            if(R == L){
                max++;
                R = 0, L = 0;
            }
        }
        return max;
    }
};