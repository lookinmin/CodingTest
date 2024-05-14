from sys import stdin
arr = list(map(str, stdin.readline().rstrip()))

stack = []

for w in arr:
    if w == '+':
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif w == '-':
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif w == '*':
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif w == '/':
        b = stack.pop()
        a = stack.pop()
        stack.append(a // b)
    else:
        stack.append(int(w))

print(stack[-1])