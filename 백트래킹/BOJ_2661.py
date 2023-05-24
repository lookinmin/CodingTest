# 좋은 수열, G4, 백트래킹

from sys import stdin
from itertools import combinations
n = int(stdin.readline())

nums = []

def dfs(idx):
    for i in range(1, (idx//2) + 1):
        # 현재 선택한 수(1,2,3 중 1)가 적합한 수 인지 판단
        if nums[-i:] == nums[-2 * i : -i]:  # 현재 체크 중인 자릿수의 절반 만큼만 반복
            return -1                       # -> 전체 수열에 대해 체크 가능

    if idx == n:        # 원하는 길이의 수 만큼 만듬
        for i in range(n):
            print(nums[i], end='')
        return 0

    for i in range(1, 4):
        nums.append(i)
        if dfs(idx + 1) == 0:       # 해당 수를 넣었을 때 완성
            return 0
        nums.pop()

dfs(0)