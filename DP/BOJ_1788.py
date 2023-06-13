# 피보나치 수의 확장, S3, DP
# 음수 피보나치

from sys import stdin

n = int(stdin.readline())
dp = [0, 1]

for i in range(2, abs(n) +1):
    dp.append((dp[i-1] + dp[i-2]) % 1000000000)

if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

print(dp[abs(n)])






# 메모리 초과 코드 -> 배열이 2개면 128MB 이상
# dp = [0, 1]     # 양수 피보나치
# zp = [0, 1]     # 음수 피보나치
#
# if n > 0:
#     print(1)
#     for i in range(2, n+1):
#         dp.append(dp[i-1] + dp[i-2])
#
#     print(abs(dp[n]) % 1000000000)
#
# elif n < 0:
#     n = n * -1
#     for i in range(2, n+1):
#         if i % 2 == 0:      # 짝수면 음수임
#             zp.append(-1 * (abs(zp[i-1]) + abs(zp[i-2])))
#         else:
#             zp.append(abs(zp[i-1]) + abs(zp[i-2]))
#
#     if zp[n] < 0:
#         print(-1)
#     else:
#         print(1)
#     print(abs(zp[n]) % 1000000000)
# else:
#     print(0)
#     print(0)
