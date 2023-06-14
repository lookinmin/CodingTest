# 비슷한 단어, S3, 구현

from sys import stdin

n = int(stdin.readline())
arr = []
res = 0
stand = list(stdin.readline().rstrip())
for _ in range(n-1):
    compare = stand[:]
    word = stdin.readline().rstrip()        # new word
    cnt = 0

    for i in word:
        if i in compare:
            compare.remove(i)       # 단어가 있으면 지운다
        else:
            cnt += 1                # 없으면 cnt를 늘린다 (2이상 되면 안됨)


    if cnt < 2 and len(compare) < 2:
        res += 1

print(res)

