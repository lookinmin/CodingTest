#include <bits/stdc++.h>

class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        unordered_map<int, int> v;
        for(int& x : deck){
            v[x]++;
        }
        
        int gcdValue = 0;
        for (const auto& x : v) {
            gcdValue = gcd(gcdValue, x.second);
        }

        return gcdValue >= 2;
    }
};