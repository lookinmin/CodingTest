# 리모콘, G5, 완탐

from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))

count = abs(100 - n)

for nums in range(1000001):
    nums = str(nums)
    for j in range(len(nums)):
        if int(nums[j]) in arr:     # 각 숫자 고장확인
            break                   # 고장이면 for문 탈출
        elif j == len(nums) - 1:    # 고장 아니고 마지막까지 왔으면
            count = min(count, abs(int(nums) - n) + len(nums))  # count 업데이트

print(count)