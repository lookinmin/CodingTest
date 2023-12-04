def solution(s):
    answer = ''
    s = list(s)
    s.sort(reverse=True)
    for w in s:
        answer += w
    return answer