#include <string>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    priority_queue<int> maxHeap;
    for(auto& x : works){
        maxHeap.push(x);
    }
    
    while(n > 0 && !maxHeap.empty()){
        int a = maxHeap.top();
        maxHeap.pop();
        if(a > 0){
            a -= 1;
            maxHeap.push(a);   
        }
        n--;
    }
    while(!maxHeap.empty()){
        int x = maxHeap.top();
        maxHeap.pop();
        answer += pow(x, 2);
    }
    return answer;
}