# 조약돌 꺼내기, S3
from sys import stdin
import math

m = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
k = int(stdin.readline())

n = sum(arr)
total = math.comb(n, k)

color = 0
for stone in arr:
    color += math.comb(stone, k)

print(color/total)