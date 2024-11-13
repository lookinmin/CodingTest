#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int cnt = 0;
    priority_queue<int> minHeap;
    
    for(auto& x : scoville){
        minHeap.push(-x);
    }
    
    while(-minHeap.top() < K){
        int a = -minHeap.top();
        minHeap.pop();
        int b = -minHeap.top();
        minHeap.pop();
        int tmp = a + (b * 2);
        minHeap.push(-tmp);
        cnt++;
        if(minHeap.size() == 1 && -minHeap.top() < K){
            return -1;
        }
    }
    return cnt;
}