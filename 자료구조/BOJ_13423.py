# Three Dots, S2
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    arr.sort()
    res = 0

    dic = dict()
    for num in arr:
        dic[num] = True

    for i in range(n-2):
        for j in range(i + 1, n - 1):
            if arr[j] * 2 - arr[i] in dic:      # arr[j]*2 를 C로 보고 B의 유무를 찾는다.
                res += 1

    print(res)