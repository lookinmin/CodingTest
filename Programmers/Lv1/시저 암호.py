def solution(s, n):
    answer = ''
    # 대문자 : 65 ~ 90
    # 소문자 : 97 ~ 122
    for w in s:
        if w == ' ':
            answer += w
        else:
            if w.islower():
                answer += chr((ord(w) - 97 + n) % 26 + 97)
            elif w.isupper():
                answer += chr((ord(w) - 65 + n) % 26 + 65)
    return answer