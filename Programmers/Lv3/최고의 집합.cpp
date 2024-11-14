#include <bits/stdc++.h>
using namespace std;

vector<int> solution(int n, int s) {
    if(s < n){
        return {-1};
    }
    
    int num = s / n;
    int rest = s % n;
    vector<int> res(n, num);
    
    if(s / num == 0){
        return {-1};
    } else {
        int idx = 0;
        while(rest > 0){
            res[idx]++;
            idx++;
            rest--;
        }
        sort(res.begin(), res.end());
        return res;
    }
}