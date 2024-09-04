from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        k = len(nums)
        total = [i for i in range(1, k + 1)]
        dic = defaultdict(int)
        res = []
        for num in nums:
            dic[num] += 1
            if dic[num] == 2:
                res.append(num)
        
        for num in total:
            dic[num] -= 1
            if dic[num] == -1:
                res.append(num)
        
        return res
        