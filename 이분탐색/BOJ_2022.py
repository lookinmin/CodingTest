# 사다리, G5, 이분탐색

from sys import stdin
x,y,c = map(float, stdin.readline().split())

start = 0
end = min(x, y)
res = 0

def f(x, y, w):
    h1 = (x**2 - w**2)**0.5     # h1 = x를 빗변으로 두는 직각삼각형의 높이
    h2 = (y**2 - w**2)**0.5     # h2 = y를 빗변으로 두는 직각삼각형의 높이
    c = h1*h2 / (h1+h2)         # 기하 -> 수학 식 세우는게 ㅈㄴ 어려움
    return c

while end - start > 0.000001:
    mid = (start + end) / 2
    if f(x, y, mid) >= c:       # 기준 탐색 값이 c보다 크거나 같은 경우
        res = mid               # 출력값 = 기준값
        start = mid             # 해당 기준값부터 이분탐색 다시
    else:
        end = mid

print("{:.3f}".format(res))