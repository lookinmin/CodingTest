from itertools import permutations

def operate(op, a, b):
    if op =='+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b

def solution(expression):
    expression = list(expression)
    tmp = []
    op_lists = list(permutations(['+', '-', '*'], 3))
    # 1. 문자열의 숫자들을 int로 변환
    i = 0
    while expression:
        if expression[i] in ['*', '+', '-']:
            k = str(''.join(expression[:i]))
            tmp.append(int(k))
            tmp.append(expression[i])
            for j in range(i+1):
                expression[j] = ''
        if '*' not in expression and '+' not in expression and '-' not in expression:
            k = str(''.join(expression[i:]))
            tmp.append(int(k))
            break
        i += 1

    # 2. 이제 우선순위에 맞춰 값 계산

    res = 0

    for op_list in op_lists:
        exp = tmp
        for op in op_list:      # 임의의 순서로 부여한 연산자 순서대로 계산
            stack = []
            for w in exp:
                if stack and stack[-1] == op:   # 제일 마지막에 들어간게 현재 순서의 연산자
                    operation = stack.pop()     # 연산자꺼내고
                    stack[-1] = operate(operation, stack[-1], w)   # 계산한 값으로 치환
                else:
                    stack.append(w)
            exp = stack
        res = max(res, abs(exp[0]))

    return res

