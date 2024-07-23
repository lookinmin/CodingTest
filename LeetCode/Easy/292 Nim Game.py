class Solution:
    def canWinNim(self, n: int) -> bool:
        # 1 ~ 3개 뺄 수 있음
        return n % 4 != 0

            