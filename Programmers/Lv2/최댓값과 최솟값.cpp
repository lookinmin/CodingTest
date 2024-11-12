#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

string solution(string s) {
    stringstream ss(s);
    string tmp;
    
    vector<int> v;
    
    while(ss >> tmp){
        v.push_back(stoi(tmp));    
    }
    
    int max = *max_element(v.begin(), v.end());
    int min = *min_element(v.begin(), v.end());
    
    string answer = to_string(min) + " " + to_string(max);
    return answer;
}