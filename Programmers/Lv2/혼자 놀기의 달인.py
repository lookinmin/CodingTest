def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = 0
        while cards[i]:
            nxt = cards[i] - 1
            cards[i], i = 0, nxt
            tmp += 1
        answer.append(tmp)

    answer.sort()
    return answer[-1] * answer[-2]