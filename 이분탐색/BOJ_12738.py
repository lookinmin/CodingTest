# 가장 긴 증가하는 부분 수열 3, G2, 이분탐색-LIS

from sys import stdin
import bisect

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

dp = [a[0]]       # 가장 긴 증가하는 부분 수열을 저장
# bisect_left(arr, x) : 정렬 순서를 유지하며 arr에 x를 삽입할 가장 왼쪽 인덱스

for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        idx = bisect.bisect_left(dp, a[i])          # dp 리스트에서 a[i]값을 찾아 해당 위치의 인덱스 리턴
        dp[idx] = a[i]                              # 해당 위치의 인덱스에 a[i]값 할당
print(len(dp))