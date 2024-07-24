class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 4 = 100 (3)
        # 16 = 10000 (5)
        # 64 = 1000000 (7)
        tmp = bin(n)[2:]
        if len(tmp) % 2 == 0:
            return False
        else:
            if tmp[0] == '1' and '1' not in tmp[1:]:
                return True
            else:
                return False
