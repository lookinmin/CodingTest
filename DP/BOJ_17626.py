# Four Squares, S3, DP - 브루트 포스
# n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하기

n = int(input())

# 브루트 포스 풀이
import math

def four_sq(n):
    if int(math.sqrt(n)) == math.sqrt(n):       # sqrt(n)이 정수
        return 1
    for i in range(1, int(math.sqrt(n))+ 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):     # sqrt(n-i^2) 이 정수
            return 2

    for i in range(1, int(math.sqrt(n))+1):     # sqrt(n - i^2 - j^2) 이 정수
        for j in range(1, int(math.sqrt(n-i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
    return 4

print(four_sq(n))