def solution(s, skip, index):
    answer = ''
    # s의 각 문자를 index만큼 증가시키는데, skip의 값들은 넘어가기

    for w in s:
        tmp = ord(w)
        cnt = 0
        while 1:
            # 97 ~ 122
            tmp = (tmp % 122) + 97
            k = chr(tmp + 1)

            if k in skip:
                continue
            else:
                print(cnt)
                cnt += 1
                tmp += 1

            if cnt == index:
                answer += (chr(tmp))
                break

    return answer


print (solution("aukks", "wbqd", 5))
