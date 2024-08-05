from collections import defaultdict
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        res = []
        for val in dic.keys():
            if dic[val] == 1:
                res.append(val)
        
        return res