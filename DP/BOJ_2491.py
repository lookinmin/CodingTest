# 수열, 실버4, 구현, LIS 중 길이가 가장 긴 것의 길이 출력
# DP로 풀이

n = int(input())
a = list(map(int, input().split()))

dp1 = [1]*n     # 증가하는지
dp2 = [1]*n     # 감소하는지

for i in range(1,n):
    if a[i-1] <= a[i]:      # 증가
        dp1[i] = max(dp1[i], dp1[i-1] + 1)
    if a[i-1] >= a[i]:    # 감소
        dp2[i] = max(dp2[i], dp2[i-1] + 1)

print(max(max(dp1), max(dp2)))