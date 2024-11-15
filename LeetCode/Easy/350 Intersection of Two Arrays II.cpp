#include <bits/stdc++.h>
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> one;
        unordered_map<int, int> two;

        for(int& x : nums1){
            one[x]++;
        }

        for(int& x : nums2){
            two[x]++;
        }

        vector<int> res;
        for(auto& pair : one){
            if(two.count(pair.first)){
                for(int i = 0; i < min(one[pair.first], two[pair.first]); i++){
                    res.push_back(pair.first);
                }
            }
        }
        return res;
    }
};