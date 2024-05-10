def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x: x[1])

    bound = 0
    for s, e in targets:
        if bound > s:
            bound = min(bound, e)
        else:
            bound = e
            answer += 1
    return answer