# 안정적인 문자열, S1, 문자열

from sys import stdin
i = 1
while 1:
    data = list(stdin.readline().rstrip())
    cnt = 0
    if '-' in data:
        break
    if data == '':
        print("{}. {}".format(i, 0))
        i += 1
        continue

    stack = []

    for w in data:
        if w == '{':
            stack.append(w)
        elif w == '}':
            if len(stack) != 0:
                stack.pop()
            else:
                stack.append('{')
                cnt += 1

    if len(stack) > 0:
        cnt += (len(stack) // 2)

    print("{}. {}".format(i, cnt))
    i += 1
