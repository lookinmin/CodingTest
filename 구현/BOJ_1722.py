# 순열의 순서, G5, 구현

from sys import stdin
from itertools import permutations
# n의 최대값이 20이므로, 20!은 시간초과 발생
# 따라서 permuatation 불가

n = int(stdin.readline())
s = list(map(int, stdin.readline().split()))
cache = {}

def find_per(n):
    if n in cache:
        return cache[n]
    elif n <= 1:
        return 1
    else:
        cache[n] = n * find_per(n-1)
        return cache[n]

if s[0] == 1:
    k = s[1]
    arr = [i for i in range(1, n+1)]
    res = []

    for i in range(n):
        x = find_per(n-1-i)
        step = (k-1) // x
        res.append(arr[step])
        arr.remove(arr[step])
        k -= x* step
    print(*res)

else:
    tmp = s[1:]
    sort_tmp = sorted(s[1:])
    cnt = 1

    for i in range(n):
        step = sort_tmp.index(tmp[i])
        sort_tmp.remove(tmp[i])
        x = find_per(n - 1 - i)
        cnt += x* step
    print(cnt)