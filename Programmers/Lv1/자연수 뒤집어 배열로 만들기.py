def solution(n):
    answer = []
    str_n = str(n)
    tmp = list(str_n)
    tmp.reverse()
    print(tmp)
    for i in tmp:
        answer.append(int(i))
    return answer