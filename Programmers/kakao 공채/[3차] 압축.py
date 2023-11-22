def solution(msg):
    answer = []
    # 1. 딕셔너리 초기화
    alpha = {}
    # 출처 : https://www.ibm.com/docs/ko/sdse/6.4.0?topic=administering-ascii-characters-from-33-126
    # 아스키 코드 참조
    for i in range(65, 91):
        alpha[chr(i)] = i - 64

    num = 27

    while msg:
        idx = 1
        while msg[:idx] in alpha and idx <= len(msg):
            idx += 1

        idx -= 1
        now = msg[:idx]
        answer.append(alpha[now])
        next = msg[:idx+1]
        alpha[next] = num
        num += 1
        msg = msg[idx : ]
    return answer

print(solution('KAKAO'))