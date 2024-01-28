import re
def solution(s):
    answer = [0, 0]  # 변환 횟수, 사라진 0의 수

    while 1:
        cnt = s.count('0')
        answer[1] += cnt
        s = re.sub('0', '', s)
        answer[0] += 1
        s = bin(len(s))[2:]
        if s == '1':
            break
    return answer