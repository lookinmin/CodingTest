#include <bits/stdc++.h>
class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        string cleaned = "";
        
        // 1. 입력 문자열에서 대시를 제거하고 대문자로 변환
        for (char c : s) {
            if (c != '-') {
                cleaned += toupper(c);
            }
        }

        reverse(cleaned.begin(), cleaned.end());
        string res = "";
        int cnt = 0;
        for(int i = 0; i < cleaned.size(); i++){
            res += cleaned[i];
            cnt++;

            if(cnt == k && i != cleaned.size() - 1){
                cnt = 0;
                res += '-';
            }
        }

        reverse(res.begin(), res.end());
        return res;
    }
};