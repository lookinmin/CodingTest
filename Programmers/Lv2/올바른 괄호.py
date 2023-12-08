def solution(s):
    answer = True

    stack = []

    for w in s:
        if w == '(':
            stack.append(w)
        else:
            if len(stack) <= 0:
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False