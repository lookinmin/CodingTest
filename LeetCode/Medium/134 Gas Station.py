class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        road = [0] * n

        for i in range(n):
            road[i] = gas[i] - cost[i]
        
        if sum(road) < 0:
            return -1

        cur, idx = 0, 0
        for i in range(n):
            cur += road[i]
            if cur < 0:
                idx = i + 1
                cur = 0
        
        return idx if cur >= 0 else -1
    