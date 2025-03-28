from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        res = []
        
        cnt = Counter(s)
        asc = sorted(cnt.keys())
        desc = asc[::-1]

        while len(res) < len(s):
            for ch in asc:
                if cnt[ch]:
                    res.append(ch)
                    cnt[ch] -= 1
            
            for ch in desc:
                if cnt[ch]:
                    res.append(ch)
                    cnt[ch] -= 1
        
        return "".join(res)