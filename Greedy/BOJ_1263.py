# 시간관리, S1, 정렬-그리디

from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

arr = sorted( arr, key= lambda x : x[1])        # 일정을 완료해야 하는 순으로 정렬 (급하니까)

time = 0        # 시작시간      (일단 0시에 시작)
while 1:
    sumTime = time
    print(time)
    for t, s in arr:
        if sumTime + t <= s:        # 일정을 제시간안에 처리 가능   (0+3) < 5 ok        -> 3+8 < 14 ok
            sumTime += t            # 그만큼 늦잠 자라             sumTime = 3         -> sumTime = 11

        else:
            print(time-1)           # 완료 못하면 -1
            exit()
    time += 1                       # 0->1->2

