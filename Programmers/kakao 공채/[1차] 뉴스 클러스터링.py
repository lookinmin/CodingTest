def solution(str1, str2):
    answer = 0
    s1 = str1.upper()
    s2 = str2.upper()

    set1 = []
    set2 = []
    # 두 단어씩 끊기
    for i in range(len(s1) - 1):
        tmp = s1[i] + s1[i + 1]
        if (65 <= ord(tmp[0]) <= 90) and (65 <= ord(tmp[1]) <= 90):
            set1.append(tmp)

    for i in range(len(s2) - 1):
        tmp = s2[i] + s2[i + 1]
        if (65 <= ord(tmp[0]) <= 90) and (65 <= ord(tmp[1]) <= 90):
            set2.append(tmp)

    # 끊었으면 교집합부터
    s2_temp = set2.copy()
    hab = set2.copy()

    gyo = []
    for w in set1:
        if w in set2:
            set2.remove(w)  # set2에서 지우고
            gyo.append(w)

    for w in set1:
        if w not in s2_temp:  # 복사해놓은 s2_temp랑 비교
            hab.append(w)
        else:
            s2_temp.remove(w)

    print(gyo)
    print(hab)

    if len(hab) == 0:
        return 65536
    else:
        div = len(gyo) / len(hab) * 65536
        return int(div)

