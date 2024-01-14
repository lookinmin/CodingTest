def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(len(s), i, -1):
            # i ~ j까지의 문자열
            tmp = s[i: j]

            if tmp == tmp[::-1]:
                answer = max(answer, len(tmp))

    # start = 0
    # end = start + 1
    #
    # while 1:
    #     tmp = s[start : end]
    #     if tmp == tmp[::-1]:
    #         answer = max(answer, len(tmp))
    #
    #
    #     if end == len(s) + 1:
    #         start += 1
    #     else:
    #         end += 1
    #
    #     if end == len(s) + 1 and start == end - 1:
    #         break

    return answer

