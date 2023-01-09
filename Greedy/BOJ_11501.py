# 주식, 그리디, 실버2
# i와 i+1 비교, 같거나 증가하는중이면 i에서 매입
# 감소하는중이면 i+1 값으로 매각

from sys import stdin
t = int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    val = 0     # 결과
    res = 0     # 가장 큰 값을 담을 변수
    for j in range(len(arr)-1, -1, -1):     # 뒤부터 역순으로
        if arr[j] > res:
            res = arr[j]
        else:
            val += res-arr[j]
    print(val)


