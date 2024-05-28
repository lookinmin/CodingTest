# 후위 표기식, G2
from sys import stdin

arr = stdin.readline().rstrip()

op = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
postfix = []
stack = []

res = ''

for w in arr:
    if 'A' <= w <='Z':
        postfix.append(w)
    elif w == '(':
        stack.append(w)
    elif w == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()
    else:
        while stack and op[w] <= op[stack[-1]]:
            postfix.append(stack.pop())
        stack.append(w)

while len(stack) != 0:
    postfix.append(stack.pop())

for val in postfix:
    res += val
print(res)