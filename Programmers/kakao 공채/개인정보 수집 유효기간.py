
def solution(today, terms, privacies):
    answer = []

    termDic = {}
    for term in terms:
        tmp = term.split(' ')
        termDic[tmp[0]] = int(tmp[1])

    dic = {}

    # 한달 28일이 정해져있어 datetime을 쓸 수 없음...

    for i in range(len(privacies)):
        tmp = privacies[i].split(' ')
        y,m,d = tmp[0].split('.')
        y = int(y)
        m = int(m)
        d = int(d)


        type = tmp[1]
        plus = termDic[type] * 28

        d = d + plus - 1

        k = d // 28
        d = (d % 28)
        if d == 0:
            d = 28
            k -= 1      # day 계산

        m = m+k

        mk = m // 12
        m = m % 12
        if m == 0:
            m = 12
            mk -= 1     # month 계산

        y = y + mk      # year 계산

        y = '{0:04d}'.format(y)
        m = '{0:02d}'.format(m)
        d = '{0:02d}'.format(d)


        cutDate = y + '.' + m + '.' + d

        dic[i+1] = cutDate

    for i in range(len(dic.keys())):
        if dic[i+1] < today:
            answer.append(i+1)


    return answer