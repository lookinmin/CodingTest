# 피보나치, S1, 그리디-수학

from sys import stdin
T = int(stdin.readline())

dp = [0] * 46
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, 46):
    dp[i] = dp[i-1] + dp[i-2]           # 피보나치 F46 > 1000000000 이므로 46까지 넣어줌

for _ in range(T):
    n = int(stdin.readline())
    res = []
    tmp = 0
    while n:
        for k in range(46):
            if dp[k] <= n:      # n보다 같거나 작은 피보나치 수를 고르고
                tmp = dp[k]     # 해당 수를 tmp로 임시 저장, (제일 큰 수가 저장됨)
        n -= tmp                # n에서 해당 수 만큼 빼주고
        res.append(tmp)         # 해당 수를 결과 배열에 저장

    res.sort()  # 결과 배열은 작은 수부터 들어가게끔 정렬
    for b in res:
        print(b, end=' ')
    print()