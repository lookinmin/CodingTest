# 주유소, S3, 그리디

from sys import stdin

n = int(stdin.readline())
way = list(map(int, stdin.readline().split()))
node = list(map(int, stdin.readline().split()))

res = 0
tmp = node[0]
for i in range(len(way)):
    if node[i]  < tmp:      # 다음 방문 주유소가 더 쌈
        tmp = node[i]
    res += tmp * way[i]     # 그 주유소에서 길이만큼 더 넣음

print(res)