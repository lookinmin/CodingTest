#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_map<string, vector<string>> closet;
    
    for(auto& cloth : clothes){
        closet[cloth[1]].push_back(cloth[0]);
    }
    
    int res = 1;
    for(auto& pair : closet){
        string key = pair.first;
        res *= (closet[key].size()+1);
    }
    res -= 1;
    return res;
}