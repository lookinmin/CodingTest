# 밥, G5
from sys import stdin

n, x = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))

arr.sort(key= lambda x : (x[0] - x[1]), reverse=True)
x -= 1000 * n
res = sum(i[1] for i in arr)

for day in arr:
    if x >= 4000 and day[0] > day[1]:
        res += (day[0] - day[1])
        x -= 4000

    else:
        break

print(res)