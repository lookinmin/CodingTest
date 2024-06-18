from sys import stdin
n = int(stdin.readline())
lectures = []
for _ in range(n):
    s, f = map(int, stdin.readline().split())
    lectures.append([s, f])

lectures.sort(key = lambda x : x[1])
cnt = 1
last = lectures[0][1]

for i in range(1, n):
    if last <= lectures[i][0]:
        cnt += 1
        last = lectures[i][1]
    else:
        continue

print(cnt)