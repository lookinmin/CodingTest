def solution(A, B):
    answer = 0
    if min(A) > max(B):
        return 0

    A.sort(reverse=True)
    B.sort(reverse=True)

    for num in A:
        if num >= B[0]:
            continue
        else:
            answer += 1
            del B[0]
    return answer