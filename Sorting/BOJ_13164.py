# 행복 유치원, G5, 정렬-그리디
from sys import stdin
n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

cost = []

for i in range(n-1):
    cost.append(arr[i+1] - arr[i])

cost.sort()     # 키 차이 작은 순 대로 정렬

print(sum(cost[:n-k]))      #  여기가 이해가 잘 안됨