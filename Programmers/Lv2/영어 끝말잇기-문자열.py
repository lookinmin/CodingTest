import math
def solution(n, words):
    answer = []

    tmp = []  # 쓴 거
    cnt = 0

    def check(cnt):
        num = cnt % n
        if num == 0:
            num = n

        return [num, math.ceil(cnt / n)]


    for word in words:
        cnt += 1  # 지금 순서
        if word not in tmp:
            if len(tmp) > 0:
                if tmp[-1][-1] == word[0]:
                    tmp.append(word)
                else:
                    return check(cnt)
            else:
                tmp.append(word)
        else:
            return check(cnt)

    answer = [0, 0]

    return answer

print(solution(	2, ["hello", "one", "even", "never", "now", "world", "draw"]))