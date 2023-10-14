# 겹치는 건 싫어, S1, 투 포인터

from sys import stdin

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

# 같은 정수를 k개 이하로 포함

s = 0
e = 0

counter = [0] * (max(arr) + 1)

res = 0

while e < n:
    if counter[arr[e]] < k:
        counter[arr[e]] += 1
        e += 1
    else:
        counter[arr[s]] -= 1
        s += 1
    res = max(res, e-s)
    # tmp = arr[s : e]
    # c = []
    # for n in range(len(tmp)):
    #     c.append(tmp.count(tmp[n]))
    #
    # if max(c) > k:
    #     continue
    #
    # nxt = arr[e+1]
    #
    # if n == len(tmp)-1:
    #     print(len(tmp))
    #     exit(0)
    #
    # if e < n-1:
    #     e += 1
    # elif e == n-1:
    #     s += 1

print(res)