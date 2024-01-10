def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()

    for num in reserve[:]:
        if num in lost:
            reserve.remove(num)
            lost.remove(num)

    for num in reserve:
        if num - 1 in lost:
            lost.remove(num - 1)
        elif num + 1 in lost:
            lost.remove(num + 1)

    return n - len(lost)