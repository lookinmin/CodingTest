#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    
    unordered_map<string, int> myMap;
    for(int i = 0; i < want.size(); i++){
        myMap[want[i]] = number[i];
    }
    
    for(int day = 0; day <= discount.size() - 10; day++){
        bool flag = true;
        unordered_map<string, int> tmp = myMap;
        
        for(int i = 0; i < 10; i++){
            if(tmp.count(discount[day + i]) && tmp[discount[day + i]] > 0){
                tmp[discount[day + i]]--;
            } else {
                flag = false;
                break;
            }
        }
        if(flag){
            answer++;
        }
    }
    return answer;
}

// ------------------- 함수로 쪼개기 ---------------------

#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

bool check(int startDay, const unordered_map<string, int>& original, const vector<string>& discount) {
    unordered_map<string, int> tmp = original;
    for(int i = 0; i < 10; i++){
        if(tmp.count(discount[startDay + i]) && tmp[discount[startDay + i]] > 0){
            tmp[discount[startDay + i]]--;
        } else {
            return false;
        }
    }
    return true;
}

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    
    unordered_map<string, int> myMap;
    for(int i = 0; i < want.size(); i++){
        myMap[want[i]] = number[i];
    }
    
    for(int day = 0; day <= discount.size() - 10; day++){
        if(check(day, myMap, discount)) answer++;
    }
    return answer;
}