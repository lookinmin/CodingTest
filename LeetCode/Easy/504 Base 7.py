class Solution:
    def convertToBase7(self, num: int) -> str:
        def cvt(num, neg):
            num = abs(num)
            if num == 0:
                return "0"
            
            base7 = []

            while num > 0:
                base7.append(str(num % 7))
                num //= 7
            
            if neg:
                base7.append('-')
            return "".join(base7[::-1])
        
        if num < 0:
            return cvt(num, True)
        else:
            return cvt(num, False)