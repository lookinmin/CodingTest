# 괄호의 값, S1, 구현, 스택

n = list(input())
stack = []
res = 0
tmp = 1 # 곱해줘야되니까

for i in range(len(n)):
    if n[i] == "(":
        stack.append(n[i])
        tmp *= 2
    elif n[i] == "[":
        stack.append(n[i])
        tmp *= 3
    elif n[i] == ")":
        if not stack or stack[-1] == "[":       # 오류
            res = 0
            break
        if n[i-1] == "(":
            res += tmp
        stack.pop()
        tmp //= 2        # 중간 계산 값 초기화
    elif n[i] == "]":
        if not stack or stack[-1] == "(":       # 오류
            res = 0
            break
        if n[i-1] == "[":
            res += tmp
        stack.pop()
        tmp //= 3       # 중간 계산 값 초기화

if stack:       # 남아있는게 있으면 오류가 있는 것
    print(0)
else:
    print(res)