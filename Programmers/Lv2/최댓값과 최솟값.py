def solution(s):
    list_s = s.split(' ')
    cvt = []
    for w in list_s:
        cvt.append(int(w))

    cvt.sort()
    answer = ''
    answer += str(cvt[0])
    answer += ' '
    answer += str(cvt[-1])
    return answer