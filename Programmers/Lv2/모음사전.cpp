#include <string>
#include <vector>
#include <set>
#include <iterator>

using namespace std;

vector<char> vowels = {'A', 'E', 'I', 'O', 'U'};
set<string> mySet;
    
void dfs(string now){
    if(now.length() > 5){
        return;
    }
    mySet.insert(now);
    for(int i = 0; i < 5; i++){
        dfs(now + vowels[i]);
    }
}

int solution(string word) {
    dfs("");
    
    auto it = mySet.find(word);
    if(it != mySet.end()){
        int idx = distance(mySet.begin(), it);
        return idx;
    }
    return -1;
}