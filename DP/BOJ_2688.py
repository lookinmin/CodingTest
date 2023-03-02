# 줄어들지 않아, S1, DP
# 각 자리 수보다 그 왼쪽 자리수가 같거나 작을 때

from sys import stdin

# 자리 수 별로 마지막수 담기
# 시작 => [0,1,2,3,4,5,6,7,8,9] 이므로 -> dp = [1] * 10
# 2자리 수 만들 때 => 각 배열의 현재 인덱스 이상의 값 전부 더하기
# dp -> [10, 9, 8, 7 ,6, 5, 4, 3, 2, 1]
# 3자리 수
# dp -> [55, 45, 36 ... ,1]
T = int(stdin.readline())
for _ in range(T):
    dp = [1] * 10
    n = int(stdin.readline())
    for i in range(n-1):
        for j in range(1, 10):
            dp[j] += dp[j-1]
    print(sum(dp))

