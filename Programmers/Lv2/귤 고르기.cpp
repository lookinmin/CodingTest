#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    unordered_map<int, int> myMap;
    
    for(int x : tangerine){
        myMap[x]++;
    }
    
    vector<int> v;
    for(auto& pair : myMap){
        v.push_back(pair.second);
    }
    
    sort(v.begin(), v.end(), greater<int>());
    
    for(int cnt : v){
        k -= cnt;
        answer++;
        if(k <= 0){
            break;
        }
    }
    return answer;
}