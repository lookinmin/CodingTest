# 에너지 드링크, S3, 그리디
from sys import stdin

n = int(stdin.readline())
drinks = list(map(int, stdin.readline().split()))

drinks.sort(reverse=True)

res = drinks[0]

for i in range(1, n):
    res = res + (drinks[i] / 2)

print(res)