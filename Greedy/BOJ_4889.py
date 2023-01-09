# 안정적인 문자열, 그리디, 실버1
from sys import stdin

answer = []

while True:
    stack = []
    arr = input()
    cnt = 0
    if '-' in arr:
        break
    for i in range(len(arr)):
        if len(stack) == 0 and arr[i] == '}':
            cnt += 1
            stack.append('{')                   # 하나를 넣어줘야함
        elif len(stack) != 0 and arr[i] == '}':
            stack.pop()
        else:
            stack.append(arr[i])
    cnt += len(stack)//2
    answer.append(cnt)

for i in range(len(answer)):
    print("{}. {}".format(i+1, answer[i]))

