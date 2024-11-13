#include <string>
#include <vector>

using namespace std;

int dfs(int num, int idx, vector<int>& numbers, int target){
    if (idx == numbers.size()) {
        return (num == target) ? 1 : 0;
    }
    
    int cnt = 0;
    cnt += dfs(num + numbers[idx], idx + 1, numbers, target);
    cnt += dfs(num - numbers[idx], idx + 1, numbers, target);
    
    return cnt;
}

int solution(vector<int> numbers, int target) {
    int res = dfs(0, 0, numbers, target);
    return res;
}