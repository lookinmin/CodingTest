# 퇴사 2, G5, DP

from sys import stdin

n = int(stdin.readline())

t, p =[],[]

for i in range(n):
    a,b = map(int, stdin.readline().split())
    t.append(a)
    p.append(b)

tmp = 0

dp = [0] * (n+1)

# 각각의 날 = 그날 상담을 시작 or 시작하지 않음
# 상담이 끝난 다음 날의 수익이 p[i] 만큼 증가
# dp = 현재까지의 수익 + 이번 상담의 수익 or 오늘 상담 끝나는 시점의 수익 중 큰 값

for i in range(n):
    tmp = max(dp[i], tmp)           # tmp는 현재까지의 수익
    if i + t[i] > n:
        continue
    dp[i + t[i]] = max(dp[i + t[i]], tmp + p[i])

print(max(dp))



# BOJ_14501 풀이, 값은 같으나 시간초과 발생
# for i in range(n):
#     for j in range(i + arr[i][0], n+1):
#         if dp[j] < dp[i] + arr[i][1]:
#             dp[j] = dp[i] + arr[i][1]

