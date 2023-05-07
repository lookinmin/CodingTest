# 숫자 할리갈리 게임, S1, 구현-deque
# 도도를 시작으로 도도와 수연이가 차례대로 자신이 가진 덱에서 가장 위에 위치한 카드를 그라운드에 숫자가 보이도록 내려놓는다.
# 가장 위에 위치한 카드의 숫자 합이 5가 되는 순간 수연
# 가장 위에 위치한 카드의 숫자가 5가 나오는 순간 도도

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

do = deque()
su = deque()


for _ in range(n):
    d, s = map(int, stdin.readline().split())
    do.append(d)
    su.append(s)

do_check = 0
su_check = 0

tmp1 = deque()            # 도도 그라운드
tmp2 = deque()            # 수연이 그라운드

for i in range(m):
    if i % 2 == 0:
        do_check = do.pop()
        tmp1.append(do_check)
    else:
        su_check = su.pop()
        tmp2.append(su_check)

    if len(do) == 0:            # 시간초과 해소하기
        print("su")
        exit()
    elif len(su) == 0:
        print("do")
        exit()

    if (do_check == 5) or (su_check == 5):        #dodo 종
        if tmp2:
            do.extendleft(tmp2)     # while로 appendleft()를 통해 일일히 넣어주는것보다 extendleft()가 더 빠르다
            su_check = 0
            tmp2 = deque()
        if tmp1:
            do.extendleft(tmp1)
            do_check = 0
            tmp1 = deque()

    elif (do_check + su_check == 5) and do_check != 0 and su_check != 0:
        if tmp1:
            su.extendleft(tmp1)
            do_check = 0
            tmp1 = deque()
        if tmp2:
            su.extendleft(tmp2)
            su_check = 0
            tmp2 = deque()

if len(do) > len(su):
    print("do")
elif len(do) < len(su):
    print("su")
else:
    print("dosu")