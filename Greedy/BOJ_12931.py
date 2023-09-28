# 두 배 더하기, G5, 그리디
from sys import stdin

# 1. 값 하나 1 증가
# 2. 모든 값 X2

n = int(stdin.readline())
A = [0] * n
B = list(map(int, stdin.readline().split()))
B.sort()
cnt = 0

while sum(B) != 0:
    flag = 0
    for i in range(n):
        if B[i] % 2 != 0 or B[i] == 0 or B[i] == 1:     # 홀수
            if B[i] == 0:
                continue
            else:
                B[i] -= 1
                cnt += 1
            flag = 1

    if flag == 0:               # 배열내에 홀수가 없어 전부 2로 나눠줄 수 있음
        for i in range(n):
            B[i] //= 2
        cnt += 1

    # if B[idx] == 1:
    #     cnt += 1
    #     B[idx] -= 1
    #     print(B)
    #
    # elif B[idx] % 2 == 0:
    #     cnt += 1
    #     for j in range(n):
    #         if B[j] > 1:
    #             B[j] //= 2
    #     print(B)
    #
    # idx += 1
    #
    # if idx == n-1:
    #     idx = 0


print(cnt)
