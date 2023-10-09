# 어두운 굴다리, S4, 구현

from sys import stdin

# 높이가 H = 좌우로 2H
n = int(stdin.readline())
m = int(stdin.readline())
x = list(map(int, stdin.readline().split()))

last = x[0]
height = x[0]       # 0~최초 가로등까지의 거리를 최초 높이로 선언

for i in range(1, len(x)):
    tmp = abs(last - x[i])      # 이전 가로등부터 다음 가로등까지의 길이

    if tmp % 2 == 0:
        tmp //= 2
    else:
        tmp = tmp//2 + 1

    height = max(height, tmp)

    last = x[i]

height = max(height, abs(n - x[len(x) - 1]))
# 마지막 가로등과 n까지의 거리와 마지막으로 비교
print(height)