# 수들의 합2, S4, 완탐, 투포인터

from sys import stdin

n, m = map(int, stdin.readline().split())
# 배열의 최대길이는 10000
arr = list(map(int, stdin.readline().split()))

res = 0

left, right = 0, 1

while n >= right >= left:     # 투포인터
    tmp = arr[left : right]     # 슬라이싱으로 투포인터 활용
    total = sum(tmp)

    if total == m:
        res += 1
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1

print(res)