from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        
        first = {}
        last = {}

        for idx, num in enumerate(nums):
            if num not in first:
                first[num] = idx
                # 해당 숫자(num) 이 등장하는 첫번째 위치
            last[num] = idx
            dic[num] += 1
        
        val = max(dic.values())
        
        res = len(nums)
        for num in dic:
            if dic[num] == val:
                # 가장 많이 등장하는 수임
                res = min(res, last[num] - first[num] + 1)
        return res