#include <string>
class Solution {
public:
    string defangIPaddr(string address) {
        string stack = "";
        for(auto& c : address){
            if(c == '.'){
                stack += "[.]";
            } else {
                stack += c;
            }
        }
        return stack;
    }
};