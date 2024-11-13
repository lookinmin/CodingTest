#include <sstream>
class Solution {
public:
    int lengthOfLastWord(string s) {
        stringstream ss(s);
        string tmp;
        
        vector<string> v;

        while(ss >> tmp){
            v.push_back(tmp);
        };

        string last = v.back();
        return last.length();
    }
};