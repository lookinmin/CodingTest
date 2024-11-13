#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    queue<int> pq;
    queue<int> sq;
    vector<int> answer;
    
    for(int pro : progresses){
        pq.push(pro);
    }
    
    for(int speed : speeds){
        sq.push(speed);
    }
    
    while(!pq.empty()){
        int day = (100 - pq.front() + sq.front() - 1) / sq.front();
        int cnt = 0;
        while(!pq.empty() && pq.front() + sq.front() * day >= 100){
            pq.pop();
            sq.pop();
            cnt++;
        }
        answer.push_back(cnt);
    }
    
    return answer;
}