# 문자열 게임2, G5, 문자열

from sys import stdin
from collections import defaultdict

t = int(stdin.readline())

for _ in range(t):
    w = stdin.readline().rstrip()
    k = int(stdin.readline())


    # 3. 어떤 문자를 정확히 K개 포함하는 가장 짧은 연속 문자열의 길이
    # -> 결국 이 경우도 양끝이 해당 문자여야 가장 짧은 연속 문자열이다.
    # 4. 문자를 정확히 K개 포함하고, s와 e가 해당 문자인 가장 긴 연속 문자열의 길이

    # 즉, 양 끝이 특정 문자인 문자열을 모두 찾고 최소, 최대 길이를 구하면 답

    word = defaultdict(list)

    for idx, char in enumerate(w):
        if w.count(char) >= k:
            word[char].append(idx)      # k번 이상 나온 알파벳에 대해 인덱스 값을 딕셔너리에 저장

    res3 = len(w) + 1
    res4 = -1

    for char, idx_list in word.items():
        if len(idx_list) == k:
            tmp = idx_list[-1] - idx_list[0] + 1
            if tmp < res3:
                res3 = tmp
            if tmp > res4:
                res4 = tmp
        elif len(idx_list) > k:
            s = 0
            while 1:
                e = s + (k-1)
                tmp = idx_list[e] - idx_list[s] + 1
                if tmp < res3:
                    res3 = tmp
                if tmp > res4:
                    res4 = tmp
                if e == (len(idx_list) - 1) :
                    break
                s += 1
    if res4 == -1 or res3 > 10000:
        print(-1)
    else:
        print(res3, res4)