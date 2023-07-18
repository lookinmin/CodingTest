# 펠린드롬?, G4, DP

from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
dp = [[0] * N for _ in range(N)]
# dp[][] == 1 -> 펠린

for i in range(N):
    for start in range(N - i):
        end = start + i

        if start == end:
            # 시작점과 끝점이 같다(글자수 = 1) 무조건 펠린드롬
            dp[start][end] = 1
        elif arr[start] == arr[end]:    # 시작 글자 == 끝글자
            if start + 1 == end:        # 문자열의 길이가 2임
                dp[start][end] = 1      # 펠린드롬
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1


for _ in range(m):
    s, e = map(int, stdin.readline().split())
    print(dp[s-1][e-1])
    # s ~ e 까지의 문자열이 펠린드롬인가? -> s+1 ~ e-1까지가 펠린드롬인가?

    # tmp = arr[s-1 : e]        인덱스 슬라이싱 방식은 시간초과
    # if tmp == tmp[::-1]:
    #     print(1)
    # else:
    #     print(0)
