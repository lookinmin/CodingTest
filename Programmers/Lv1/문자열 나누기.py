def solution(s):
    answer = 0
    dict = {}
    for w in s:
        if len(dict.keys()) > 0:
            tmp = list(dict.keys())[0]
            if w == tmp:
                dict[w] += 1
            else:
                dict['else'] = dict.get('else', 0) + 1
        else:
            dict[w] = 1

        if len(dict.keys()) == 2 and len(set(dict.values())) == 1:
            answer += 1
            dict = {}

    if len(dict.keys()) != 0:
        answer += 1
    return answer