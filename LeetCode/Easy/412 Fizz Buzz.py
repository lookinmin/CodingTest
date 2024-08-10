class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        def prime_factor(num):
            factors = []
            i = 2
            while i <= num:
                if num % i == 0:
                    factors.append(i)
                    num //= i
                else:
                    i += 1
            return factors

        for i in range(1, n + 1):
            tmp = prime_factor(i)
            if 3 in tmp and 5 in tmp:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        
        return res