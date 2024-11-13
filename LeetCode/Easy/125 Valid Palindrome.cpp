#include <cctype>
#include <algorithm>

class Solution {
public:
    bool isPalindrome(string s) {
        string cvt = "";
        for(char& w : s){
            if(isalnum(w)){
                cvt += tolower(w);
            }
        }
        
        string tmp = cvt;
        reverse(cvt.begin(), cvt.end());
        return tmp == cvt;
    }
};