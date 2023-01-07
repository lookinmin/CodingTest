# 병든 나이트, 실버3, 구현-그리디

from sys import stdin

n, m = map(int, stdin.readline().split())
# 무조건 오른쪽으로는 이동, 위 아래 선택

if n == 1:
    print(1)        # 이동 불가
elif n == 2:
    print(min(4, (m-1)//2 + 1))
elif m <= 6:
    print(min(4, m))
else:
    print(m-2)