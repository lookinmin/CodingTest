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

import heapq
def sol(a, b):
    a = [-i for i in a]
    b = [-i for i in b]
    # 최대힙을 위해 그냥 원소를 음수로 바꿔버림

    heapq.heapify(a)
    heapq.heapify(b)

    answer = 0

    while b and a:
        num_a = heapq.heappop(a)
        num_b = heapq.heappop(b)

        if -num_a < -num_b:
            answer += 1
        else:
            heapq.heappush(b, num_b)
    return answer