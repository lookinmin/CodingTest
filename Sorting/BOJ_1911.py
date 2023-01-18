# 흙길 보수하기, 실버1, 정렬

from sys import stdin
n,l = map(int, stdin.readline().split())
# n = 물 웅덩이 갯수, l = 널빤지의 크기
pool = [list(map(int, input().split())) for _ in range(n)]
pool.sort()
cnt = 0

for i in range(len(pool)):
    length = pool[i][1] - pool[i][0]        # 웅덩이의 길이
    if i == len(pool) - 1:                  # 마지막 웅덩이
        cnt += (length - 1) // l + 1
        break
    if length % l > 0 :                     # 널빤지가 웅덩이 크기와 맞아떨어지지 않음
        tmp = l - (length % l)              # tmp = 현재 널빤지의 위치
        now = pool[i][1] + tmp              # 현재 웅덩이의 마지막 + tmp 만큼 웅덩이 증가
        if pool[i + 1][0] <= now:
            pool[i + 1][0] = now
        cnt += (length // l) + 1
    else:                                   # 널빤지가 웅덩이 크기와 딱 맞음
        cnt += length // l

print(cnt)