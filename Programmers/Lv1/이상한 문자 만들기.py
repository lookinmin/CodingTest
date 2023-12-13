def solution(s):
    answer = ''
    arr = s.split(' ')
    for word in arr:
        tmp = ''
        for i in range(len(word)):
            if i % 2 == 0:  # 짝수
                tmp += word[i].upper()
            else:
                tmp += word[i].lower()
        answer += (tmp + " ")

    answer = answer[:-1]
    return answer