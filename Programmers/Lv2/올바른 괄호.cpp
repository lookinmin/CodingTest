#include <string>
#include <iostream>
#include <vector>

using namespace std;

bool solution(string s)
{
    vector<char> stack;
    
    for(char w : s){
        if(w == '('){
            stack.push_back(w);
        } else {
            if(stack.empty()){
                return false;
            }
            stack.pop_back();
        }
    }

    return stack.empty();
}