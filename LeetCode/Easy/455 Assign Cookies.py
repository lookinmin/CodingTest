from collections import deque
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0 or len(g) == 0:
            return 0

        s.sort(reverse = True)
        g.sort(reverse = True)

        idx1 = 0
        idx2 = 0
        cnt = 0

        while idx1 < len(g) and idx2 < len(s):
            if g[idx1] <= s[idx2]:
                cnt += 1
                idx1 += 1
                idx2 += 1
            else:
                idx1 += 1
        return cnt