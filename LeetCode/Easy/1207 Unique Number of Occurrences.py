from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)

        val = set()
        for x in counter.values():
            if x in val:
                return False
            else:
                val.add(x)
        
        return True