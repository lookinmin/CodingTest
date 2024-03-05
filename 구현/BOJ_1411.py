# 비슷한 단어, S2, 구현
from sys import stdin

n = int(stdin.readline())
tmp = [[] for _ in range(n + 1)]
dic = [{} for i in range(n + 1)]
cnt = 0

for i in range(n):
    num = 0
    words = stdin.readline().rstrip()

    for w in words:
        if w not in dic[i]:
            dic[i][w] = str(num)
            num += 1
        tmp[i] += dic[i][w]


for i in range(n):
    for j in range(i + 1, n):
        if tmp[i] == tmp[j]:
            cnt += 1

print(cnt)