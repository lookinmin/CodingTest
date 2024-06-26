import sys
input = sys.stdin.readline

n = int(input())
dp = [[0,0] for _ in range(n)]

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
dp[0] = [arr[0][0],arr[0][1]]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][0],dp[i-1][1]+arr[i-1][3])+arr[i][0]
    dp[i][1] = min(dp[i-1][1],dp[i-1][0]+arr[i-1][2])+arr[i][1]

print(min(dp[-1]))