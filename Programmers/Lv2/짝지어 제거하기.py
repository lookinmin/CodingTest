# 시간초과 발생

def solution(s):
    s = list(s)


    while len(s) > 0:
        k = len(s)
        origin = s
        for i in range(k - 1):
            tmp = s[i: i + 2]

            if tmp[0] == tmp[1]:
                s[i] = ''
                s[i+1] = ''
                break
        s = [v for v in s if v]
        if origin == s:
            return 0

    return 1

# Stack을 통한 풀이

def solution(s):
    stack = []
    for w in s:
        if len(stack) == 0:
            stack.append(w)
        elif stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    if len(stack) == 0:
        return 1
    else:
        return 0