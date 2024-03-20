#포스택, G5
from sys import stdin

stack = [[] for _ in range(4)]
N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

flag = True

for num in arr:
    for i in range(4):
        if not stack[i]:
            stack[i].append(num)
            break
        else:
            if stack[i][-1] < num:
                stack[i].append(num)
                break
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")