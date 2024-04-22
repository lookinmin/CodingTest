# 도키도키 간식드리미, S3
from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = deque(list(map(int, stdin.readline().split())))
stack = []
target = 1      # 찾는 값

while arr:
    if target == arr[0]:
        # 현재 큐의 top이 찾는 값
        arr.popleft()
        target += 1

    elif len(stack) > 0 and target == stack[-1]:
        # 스택의 top 값이 현재 찾는 값
        stack.pop()
        target += 1

    else:
        if len(stack) == 0 or (len(stack) > 0 and stack[-1] > arr[0]):
            # 스택에 들어있는 값보단 작은데 현재 찾는 target이 아님
            # target이 아닌 값인데, 현재 스택이 비어있음
            stack.append(arr.popleft())
        else:
            print("Sad")
            exit()

if len(stack) > 0:
    while stack:
        if target == stack[-1]:
            stack.pop()
            target += 1
        else:
            print("Sad")
            exit()

print("Nice" if not stack else "No")