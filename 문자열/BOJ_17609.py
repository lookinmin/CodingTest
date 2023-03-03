# 회문, G5, 문자열-투포인터

from sys import stdin
import math

T = int(stdin.readline())

def find(st):
    if st == st[::-1]:
        return 0
    else:
        start = list(st)
        end = list(st)

        for i in range(math.ceil(int(len(st)/2))):
            if st[i] != st[-(i+1)]:         # 진행하다가 다른 부분의 위치를 빼버리기
                start.pop(i)                # 양쪽 다
                end.pop(-(i+1))

                if start == start[::-1]:
                    return 1

                if end == end[::-1]:
                    return 1

                return 2
for _ in range(T):
    this = str(stdin.readline().rstrip())

    print(str(find(this)))