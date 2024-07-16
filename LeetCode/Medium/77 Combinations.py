from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, n + 1)]
        for comb in combinations(nums, k):
            res.append(list(comb))
        return res