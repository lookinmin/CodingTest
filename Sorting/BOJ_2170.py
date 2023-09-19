# 선 긋기, G5, 정렬

from sys import stdin
from collections import Counter
# 여러 번 그은 곳과 한 번 그은 곳의 차이를 구별 X

n = int(stdin.readline())
lines = list(tuple(map(int, stdin.readline().split())) for _ in range(n))
# 튜플이 리스트보다 인덱싱하는 과정이 빠르다
    # 최대가 10억

lines.sort()
start = lines[0][0]
end = lines[0][1]
# 맨 처음거 기준

res = 0

for i in range(1, n):
    nowS, nowE = lines[i]

    if end > nowS:      # 다음 시작 점이 이전 끝 점보다 앞
        end = max(end, nowE)

    else:
        res += (end-start)
        start, end = nowS, nowE

res += (end-start)
print(res)