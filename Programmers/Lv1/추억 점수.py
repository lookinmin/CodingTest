# 추억점수 Lv1
def solution(name, yearning, photo):
    answer = []

    match = dict()

    for i in range(len(name)):
        match[name[i]] = yearning[i]

    for arr in photo:
        s = 0
        for n in arr:
            if n in match:
                s += match[n]
            else:
                s += 0
        answer.append(s)
    return answer