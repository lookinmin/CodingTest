# 1, S3, 수학-완탐
from sys import stdin

while 1:
    try:
        n = int(stdin.readline().rstrip())
    except:
        break

    num = 0
    i = 1
    while 1:
        num = num*10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1