def solution(arr):
    answer = []
    tmp = []

    for w in arr:
        if len(tmp) <= 0:
            tmp.append(w)
        else:
            if tmp[-1] != w:
                answer.extend(tmp)
                tmp.clear()
                tmp.append(w)

    answer.extend(tmp)

    return answer