from typing import List
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        toBin = ''
        for num in nums:
            toBin += str(num)
            cvt = int(toBin, 2)
            
            if cvt % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        
        return res

