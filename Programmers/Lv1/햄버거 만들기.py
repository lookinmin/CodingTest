def solution(ingredient):
    # 빵 - 야채 - 고기 - 빵
    # 1 = 2 = 3
    stack = []
    answer = 0

    for i in ingredient:
        stack.append(i)

        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                stack.pop()

    return answer