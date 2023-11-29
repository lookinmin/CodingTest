def solution(s):
    answer = []
    dic = {}

    for idx in range(len(s)):
        if s[idx] in dic:
            tmp = idx - dic[s[idx]]
            dic[s[idx]] = idx
            answer.append(tmp)

        else:
            answer.append(-1)
            dic[s[idx]] = idx

    return answer



print("TC1")
print(solution("banana"))
print("TC2")
print(solution("foobar"))