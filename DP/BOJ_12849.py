# 본대 산책, S1, DP-그래프
# bottom-up
# i분 째에 건물 A에 도착하는 경우의 수 = (i-1)분 째에 건물 A와 이어진 건물들에 도착하는 경우의 수의 합

from sys import stdin

d = int(stdin.readline().rstrip())

dp = [1,0,0,0,0,0,0,0]

def move(state):
    tmp = [0] * 8
    tmp[0] = state[1] + state[3]
    tmp[1] = state[0] + state[2] + state[3]
    tmp[2] = state[1] + state[3] + state[4] + state[5]
    tmp[3] = state[0] + state[1] + state[2] + state[5]
    tmp[4] = state[2] + state[5] + state[6]
    tmp[5] = state[2] + state[3] + state[4] + state[7]
    tmp[6] = state[4] + state[7]
    tmp[7] = state[5] + state[6]

    for i in range(8):
        tmp[i] %= 1000000007
    return tmp

for i in range(d):
    dp = move(dp)

print(dp[0])