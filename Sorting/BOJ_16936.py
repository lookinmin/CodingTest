# 나3고2, G5, 수학-정렬
# 해 구성하기 - 첫 시도

from sys import stdin

# 연산 2개
# 1. 나3 = x // 3
# 2. 곱2 = x * 2

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
res = []

for num in arr:
    # 3과 2는 서로소(서로 독립)
    # 3으로 나눌 수 있는게 클 수록 앞으로,

    can3 = 0
    num_origin = num

    while 1:
        if num % 3 == 0:
            can3 += 1
            num //= 3
        else:
            break
    res.append([can3, num_origin])

res.sort(key= lambda x : (-x[0], x[1]))     # 3으로 나눈 값들이 앞에 수를 달아서 res에 들어가는데, 이때 큰 수가 앞에 있어야 해당 수를 나눠 다음 수를 만들 수 있으므로 내림차순으로 넣는다.
for i in range(n):
    print(res[i][1], end=' ')
