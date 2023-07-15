# 집합, S5, 비트마스킹

# 비트마스킹 방법으로 풀기
# &, ^, |, ~, <<, >> 사용

from sys import stdin
m = int(stdin.readline())
bit = 0
# x의 범위가 1~20이므로 길이가 20인 비트를 생각할 것

for _ in range(m):

    cal= stdin.readline().split()

    if cal[0] == "add":
        bit |= (1 << int(cal[1]) - 1)       # 비트의 해당 값에 or 연산
    elif cal[0] == "remove":
        bit &= ~(1 << int(cal[1]) - 1)      # 비트의 해당 값에 and연산 (not 한 값이랑)
    elif cal[0] == "check":
        if bit & (1 << int(cal[1]) - 1) == 0:
            print(0)
        else:
            print(1)
    elif cal[0] == "toggle":
        bit = bit ^ (1 << int(cal[1]) - 1)  # 1이면 0, 0이면 1
    elif cal[0] == "all":
        bit = (1 << 20) - 1     # 20자리수 전부 1로 바꿈
        # print(bin(bit))
    elif cal[0] == "empty":
        bit = 0
