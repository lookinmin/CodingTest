class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        total = 1
        sqrt = int(num**0.5)

        for i in range(2, sqrt + 1):
            if num % i == 0:
                total += i
                if i != num // i:       # 2와 14가 다름
                    total += num // i   # 그럼 2, 14를 둘다 더함
        
        return total == num