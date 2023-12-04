def solution(citations):

    citations.sort(reverse=True)
    # 6 5 3 1 0

    k = len(citations)
    for i in range(k):
        if citations[i] < i+1:
            return i

    return k


print(solution([3,0,6,1,5]))