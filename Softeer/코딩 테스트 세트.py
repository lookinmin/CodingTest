from sys import stdin
from collections import defaultdict
n, t = map(int, stdin.readline().split())

def test(value):
    now = c[0]
    for i in range(n - 1):
        if now >= value:
            now = c[i+1] + d[i]
        elif now + d[i] >= value:
            now = c[i+1] + (now + d[i] - value)
        else:  # 두개 더한게 value보다 작음
            return False
    if now >= value:
        return True
    else:
        return False

def binary(start, end):
    if start == end:
        return start
    mid = (start + end + 1) // 2
    if test(mid):
        return binary(mid,end)
    else:
        return binary(start, mid - 1)
            
# 난이도는 1~n
for _ in range(t):
    lst = list(map(int, stdin.readline().split()))
    # 시간복잡도가 10^9 이상 -> 단순 탐색으로는 풀 수 없다.
    # 이진 탐색 = logN
    c = [0] * (n-1)
    d = [0] * (n-1)

    for i in range(n - 1):
        c[i] = lst[2 * i]
        d[i] = lst[2*i+1]
    c.append(lst[-1])

    print(binary(0, 2*10**12))
