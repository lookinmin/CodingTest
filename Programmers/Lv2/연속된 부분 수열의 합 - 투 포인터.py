def solution(sequence, k):
    start = end = 0
    answer = [0, len(sequence)]
    sum_seq = sequence[0]

    while 1:
        if sum_seq < k:
            end += 1
            if end == len(sequence):
                break
            sum_seq += sequence[end]
        else:
            if sum_seq == k:
                if end - start < answer[1] - answer[0]:
                    answer = [start, end]
            sum_seq -= sequence[start]
            start += 1

    return answer