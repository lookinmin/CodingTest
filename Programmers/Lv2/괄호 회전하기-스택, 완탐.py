def solution(s):
    answer = 0

    k = len(s)

    for i in range(k):
        tmp = s[i:] + s[:i]
        stack = []

        for w in tmp:
            if len(stack) > 0:
                if stack[-1] == '[' and w == ']':
                    stack.pop()
                elif stack[-1] == '{' and w == '}':
                    stack.pop()
                elif stack[-1] == '(' and w == ')':
                    stack.pop()
                else:
                    stack.append(w)
            else:
                stack.append(w)
        if len(stack) == 0:
            answer += 1


    return answer

print(solution("{(})"))