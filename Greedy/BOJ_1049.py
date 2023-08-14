# 기타줄, S4, 그리디

from sys import stdin

n, m = map(int, stdin.readline().split())
# n개의 기타줄 사야됨

guitar = []
for i in range(m):
    guitar.append(list(map(int, stdin.readline().split())))

one = int(1e9)
all = int(1e9)
for i in range(m):
    one = min(one, guitar[i][1])
    all = min(all, guitar[i][0])


res = min(one*n, (n//6)*all + one*(n%6), (n//6 + 1)*all)

print(res)
