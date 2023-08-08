# 토너먼트, S4, 수학-완탐

from sys import stdin

n, kim, im = map(int, stdin.readline().split())

cnt = 0

# 8 -> 4 -> 2 -> 1      # //2씩
# 3 -> 1 -> 1 -> 1

while kim != im:
    kim = kim - kim//2
    im = im - im//2
    cnt += 1

print(cnt)