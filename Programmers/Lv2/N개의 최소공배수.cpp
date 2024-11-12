#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int solution(vector<int> arr) {
    int answer = 0;
    sort(arr.begin(), arr.end(), greater<int>());
    
    while(arr.size() > 1){
        int a = arr.back();
        arr.pop_back();
        int b = arr.back();
        arr.pop_back();
        int val = lcm(a, b);
        arr.push_back(val);
    }
    return arr[0];
}