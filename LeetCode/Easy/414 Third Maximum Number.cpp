#include <bits/stdc++.h>
class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> s(nums.begin(), nums.end());
        if(s.size() < 3){
            return *s.rbegin();
        }
        auto it = s.rbegin();
        advance(it, 2);
        return *it;
    }
};


// ----------------- 시간 우수 솔루션
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        nums.erase(unique(nums.begin(), nums.end()), nums.end());
        if(nums.size() < 3) return nums[0];
        return nums[2];
    }
};
