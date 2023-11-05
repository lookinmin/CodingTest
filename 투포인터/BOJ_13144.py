# List of Unique Numbers, G4, 투포인터

from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

s = 0
e = 0
check = [False] * 100001
res = 0
while e < n:
    if not check[arr[e]]:
        check[arr[e]] = True
        e += 1
    else:
        res += (e - s)
        check[arr[s]] -= 1
        s += 1

    # tmp = arr[s : e]
    #
    # if len(tmp) == len(set(tmp)):     # 시간초과 발생
    #     print(*tmp)
    #     res += 1
    #
    # if e < n:
    #     e += 1
    # else:
    #     s += 1
res += ((e-s) * (e-s+1)) // 2
print(res)