class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        unordered_map<char, char> brackets = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        for(char& w : s){
            if(brackets.find(w) == brackets.end()){
                st.push(w);
                // 여는 괄호
            } else {
                if(!st.empty() && st.top() == brackets[w]){
                    st.pop();
                } else {
                    return false;
                }
            }
        }

        return st.empty();
    }
};