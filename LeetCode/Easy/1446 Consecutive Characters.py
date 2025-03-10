class Solution:
    def maxPower(self, s: str) -> int:
        prev = s[0]
        res = 1
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == prev:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
                prev = s[i]
        
        return max(res, cnt)