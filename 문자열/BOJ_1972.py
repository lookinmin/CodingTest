# 놀라운 문자열, S3

from sys import stdin

while 1:
    words = stdin.readline().rstrip()
    if words == '*':
        break

    k = len(words)
    for cnt in range(1, k-1):
        tmp = set()

        for i in range(k - cnt):
            word = words[i] + words[i + cnt]
            if word in tmp:
                print("{} is NOT surprising.".format(words))
                break
            else:
                tmp.add(word)
        else:
            continue
        break
    else:
        print("{} is surprising.".format(words))

