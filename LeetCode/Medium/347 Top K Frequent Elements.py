class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)

        for num in nums:
            table[num] += 1
        
        tmp = sorted(table.items(), key = lambda x : x[1], reverse = True)
        res = []

        for i in range(k):
            res.append(tmp[i][0])
        
        return res
