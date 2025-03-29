from collections import Counter
class Solution:
    def maxScore(self, s: str) -> int:
        counter = Counter(s)
        left = 0                # 왼쪽에 있는 0의 갯수
        right = counter['1']    # 오른쪽에 있는 1의 갯수

        res = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            res = max(res, left + right)
        
        return res
