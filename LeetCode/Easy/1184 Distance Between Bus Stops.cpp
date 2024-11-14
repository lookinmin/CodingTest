#include <algorithm>
#include <vector>

class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        int n = distance.size();
        if(start > destination) swap(start, destination);

        int clock = 0;
        int reClock = 0;

        for(int i = start; i < destination; ++i){
            clock += distance[i];
        }

        for(int i = destination; i < n; ++i){
            reClock += distance[i];
        }
        for(int i = 0; i < start; ++i){
            reClock += distance[i];
        }

        return min(clock, reClock);
    }
};