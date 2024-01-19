def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        stack = []
        for w in tree:
            if w in skill:
                stack.append(w)
        flag = True
        for i in range(len(stack)):
            if stack[i] != skill[i]:
                flag = False
            if not flag:
                break
        if flag:
            answer += 1

    return answer