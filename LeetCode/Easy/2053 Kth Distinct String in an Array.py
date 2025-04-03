class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # sort the array with the frequency of each element
        arr = sorted(arr, key = lambda x: arr.count(x))
        tmp = []
        for num in arr:
            if arr.count(num) == 1:
                tmp.append(num)
            else:
                break
        
        return tmp[k-1] if k <= len(tmp) else ""

#now, it is too slow, we need to optimize it
#we can use a hash map to store the frequency of each element
#and then return the kth distinct element

from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        for num in arr:
            if freq[num] == 1:
                k -= 1
                if k == 0:
                    return num
        return ""

