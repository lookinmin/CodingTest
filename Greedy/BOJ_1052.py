# 물병, S1, 그리디
# 상점에서 사야하는 물병의 갯수, 각 물병은 하나 살 떄 마다 1L

from sys import stdin
n, k  = map(int, stdin.readline().split())
# 물병 n개를 k개로 만들기
# n을 2의 제곱으로 표현 -> 1의 개수 세기

cnt = 0

# ex) 3, 1 -> 0011(2) = 1의 개수가 2개 따라서, +1
# ex) 4, 1 -> 0100(2) = 1의 개수가 1개 따라서, +1안함

while bin(n).count('1') > k:
    n += 1
    cnt += 1

print(cnt)