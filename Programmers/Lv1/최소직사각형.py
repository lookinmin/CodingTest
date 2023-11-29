def solution(sizes):
    answer = 0

    w = []
    h = []

    n = len(sizes)
    for i in range(n):
        if sizes[i][0] > sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    answer = max(w) * max(h)
    # 최대한 작게


    return answer

print('TC1')
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print('TC2')
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))