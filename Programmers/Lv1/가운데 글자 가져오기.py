def solution(s):
    answer = ''
    k = len(s)
    tmp = k // 2
    if k % 2 == 0:
        # 문자열의 길이가 짝수
        return s[tmp-1 : tmp+1]
    else:
        return s[tmp:tmp+1]