

def solution(new_id):
    answer = ''

    new_id = list(new_id)

    # 1. 대문자 -> 소문자
    for i in range(len(new_id)):
        if new_id[i].isalpha():
            new_id[i] = new_id[i].lower()
        if new_id[i] not in ['-', '_', '.']:
            if new_id[i].isalpha() == False and new_id[i].isdigit() == False:
                new_id[i] = ''
    tmp = ''
    for i in new_id:        # 공백 제거
        tmp += i

    tmpDot = tmp.split('.')     # 연속된 점 제거
    tk = ''
    for word in tmpDot:
        if word != '':
            word = '.' + word
            tk += word

    if len(tk) > 0 and tk[0] == '.':
        tk = tk[1:]

    if len(tk) == 0:
        tk = 'a'
    if len(tk) >= 16:
        tk = tk[:15]

    if len(tk) <= 2:
        w = tk[-1]
        while len(tk) < 3:
            tk += w

    if tk[-1] == '.':
        tk = tk[:len(tk)-1]

    return tk

print(solution("abcdefghijklmn.p"))