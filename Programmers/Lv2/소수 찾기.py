import math
from itertools import permutations

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    nums = list(numbers)
    tmp = []
    for i in range(1, len(nums) + 1):
        tmp += list(permutations(nums, i))
    tmp = set(tmp)
    for num in tmp:
        k = int(''.join(num))
        if k > 1 and isPrime(k):
            answer.add(k)
    return len(answer)