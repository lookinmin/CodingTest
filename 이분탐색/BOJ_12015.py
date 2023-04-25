# 가장 긴 증가하는 부분 수열 2, G2, 이분탐색 - LIS : O(n log n)
import bisect
from sys import stdin
n = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))

# dp로 풀면 시간초과가 난다.
# dp 풀이법 = O(n^2)
dp = [1 for i in range(n)]      # dp 배열을 1로 초기화

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:     # 현재 위치보다 이전의 원소가 더 작은지 판단한다
            dp[i] = max(dp[i], dp[j] + 1)       # 작다면, 이전의 dp 최댓값을 구하고 그 길이에 1을 더한다.
print(max(dp))

# 이분탐색 LIS 풀이법, bisect 사용하기
dp = [arr[0]]       # 가장 긴 증가하는 부분 수열을 저장
# bisect_left(arr, x) : 정렬 순서를 유지하며 arr에 x를 삽입할 가장 왼쪽 인덱스
for i in range(n):
    if arr[i] > dp[-1]:     # 현재 위치가 가장 마지막 원소 보다 크면
        dp.append(arr[i])   # dp에 추가한다
    else:                   # 작거나 같으면
        idx = bisect.bisect_left(dp, arr[i])        # 이전 위치의 원소 중 가장 큰 원소의 idx 값을 구함
        dp[idx] = arr[i]        # dp[idx] 값을 arr[i]값으로 바꿔준다.
print(len(dp))

