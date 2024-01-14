def solution(elements):
    answer = 0
    k = len(elements)
    elements *= 2
    tmp = set()
    for i in range(1, k+1):
        for idx in range(k):
            tmp.add(sum(elements[idx : idx + i]))
    return len(tmp)