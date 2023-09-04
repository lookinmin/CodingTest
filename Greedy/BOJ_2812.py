# 크게 만들기, G3, 그리디

from sys import stdin

n, k = map(int, stdin.readline().split())
num = list(stdin.readline().rstrip())

stack = []
cnt = 0
for n in num:
    while stack and stack[-1] < n and k > 0:        # stack안에 값이 있고, 마지막 값이 t보다 작고, 제거횟수가 남았다면
        stack.pop()     # 마지막 값 버리고
        k -= 1          # 제거횟수 - 1
    stack.append(n)     # 시작부터 값 넣어줌

if k > 0:   # 제거 횟수가 남음
    for i in range(k):
        stack.pop()

print(''.join(stack))
