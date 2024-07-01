class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = str(num)
            num = [int(j) for j in num]
            num = sum(num)
        return num
        