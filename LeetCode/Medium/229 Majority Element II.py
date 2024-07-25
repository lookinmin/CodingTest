from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        n = len(nums) // 3
        res = []
        for num in nums:
            dic[num] += 1

            if dic[num] > n:
                if num not in res:
                    res.append(num)
        
        return res