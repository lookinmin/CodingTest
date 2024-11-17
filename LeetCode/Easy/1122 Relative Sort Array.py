from collections import defaultdict, Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)

        res = []
        for num in arr2:
            res.extend([num] * counter[num])
            del counter[num]
        
        tmp = []
        for key, value in counter.items():
            tmp.extend([key]*value)
        tmp.sort()
        res.extend(tmp)

        return res



