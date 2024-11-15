#include <bits/stdc++.h>
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string ss = s + s;
        if(ss.substr(1, ss.size() - 2).find(s) == string::npos){
            return false;
        } else {
            return true;
        }
    }
};