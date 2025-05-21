def solution(wallet, bill):
    answer = 0
    max_tmp = max(bill[0], bill[1])
    min_tmp = min(bill[0], bill[1])
    while True:
        if max_tmp <= max(wallet[0], wallet[1]) and min_tmp <= min(wallet[0], wallet[1]):
            return answer
        else:
            max_tmp //= 2
            if max_tmp < min_tmp:
                max_tmp, min_tmp = min_tmp, max_tmp
            answer+=1