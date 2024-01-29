def check(s):
    stack = []

    for w in s:
        if w == '(':
            stack.append(w)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True


def divide(s):  # 문자열을 u, v로 나누기
    left, right = 0, 0

    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return s[:i + 1], s[i + 1:]


def solution(p):
    if len(p) == 0:
        return ''

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        res = '('
        res += solution(v)  # 재귀
        res += ')'

        for w in u[1: len(u) - 1]:  # 앞뒤 버림
            if w == '(':
                res += ')'
            else:  # 괄호 방향 뒤집어서 붙임
                res += '('
        return res
