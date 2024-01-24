def solution(n, s):
    answer = []
    if s < n == 0:
        return [-1]

    num = s // n
    if s // n == 0:
        return [-1]

    rest = s % n

    for i in range(n):
        answer.append(num)
        # 수만큼 일단 half 값 넣기

    if rest != 0:
        for i in range(len(answer)):
            answer[i] += 1
            rest -= 1
            if rest == 0:
                break
    answer.sort()
    return answer