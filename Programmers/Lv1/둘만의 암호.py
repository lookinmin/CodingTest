# 둘만의 암호, Lv 1
def solution(s, skip, index):
    answer = ''
    # s의 각 문자를 index만큼 증가시키는데, skip의 값들은 넘어가기

    for w in s:

        tmp = ord(w)
        cnt = index
        while cnt > 0:
            tmp += 1
            if tmp > ord('z'):
                tmp = ord('a')
            if chr(tmp) in skip:
                cnt += 1  # 한번 더 가면 됨
            cnt -= 1

        answer += chr(tmp)
    return answer


