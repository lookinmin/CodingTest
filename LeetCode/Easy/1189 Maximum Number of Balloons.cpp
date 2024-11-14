#include <unordered_map>
#include <string>
#include <limits>

class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> balloon = {
            {'b', 0},
            {'a', 0},
            {'l', 0}, // /2
            {'o', 0}, // /2
            {'n', 0}
        };

        for(char& c : text){
            if(balloon.count(c)){
                balloon[c] += 1;
            }
        };

        balloon['l'] /= 2;
        balloon['o'] /= 2;

        int res = numeric_limits<int>::max();

        for(auto& v : balloon){
            res = min(res, v.second);
        };

        return res;
    }
};