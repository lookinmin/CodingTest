# 동전, G5, DP
# 동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성하시오.

from sys import stdin

T = int(stdin.readline())

# 동전이 오름차순으로 정렬되어 주어지기 때문에 작은 동전부터 해당 동전을 이용하여 m 원을 만들 수 있는 경우의 수를 더한 뒤,
# 다음 동전으로 넘어가서 이전 경우의 수에 해당 동전으로 만들 수 있는 경우의 수를 순차적으로 더해가며 답을 구한다.

for _ in range(T):
    n = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    dp = [0] * (m+1)
    dp[0] = 1

    for coin in coins:
        for i in range(m+1):
            if i - coin >= 0:       # 일단 만들고자 하는 값에서 냅다 동전 만큼 빼버리기 해당 값이 0 이상이면
                dp[i] += dp[i-coin] # 나머지 값을 만들 수 있는 가지수를 dp table에서 가져옴
    print(dp[m])
