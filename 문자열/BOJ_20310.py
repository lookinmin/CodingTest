# 타노스, S3, 문자열-그리디

from sys import stdin
from itertools import permutations

s = stdin.readline().rstrip()

# cntOne = s.count('0')
# cntTwo = s.count('1')
#
# tmp = []
# for i in range(cntOne // 2):
#     tmp.append(0)
# for i in range(cntTwo // 2):
#     tmp.append(1)
#
# arr = permutations(tmp, len(tmp))
# res = set()
# for w in arr:
#     k = ''
#     for i in w:
#         k += str(i)
#     res.add(k)
#
# res = list(res)
# res.sort()
#
# # print(res)
# for num in res:
#     if (num[0::2].count('1') == 0) and (num[1::2].count('0') == 0):
#         print(num)
#         exit(0)


def solution(s):

    s = list(s)
    cntOne = s.count('0') // 2
    cntTwo = s.count('1') // 2

    for _ in range(cntOne):
        s.pop(-(s[::-1].index('0')) - 1)
    for _ in range(cntTwo):
        s.pop(s.index('1'))

    print(''.join(s))

solution(s)
