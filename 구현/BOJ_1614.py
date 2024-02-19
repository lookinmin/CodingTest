# 영식이의 손가락, S3

from sys import stdin

finger = int(stdin.readline().rstrip())
num = int(stdin.readline().rstrip())
res = 0

if num == 0:
    res = finger - 1
    print(res)
    exit()

if finger == 1:
    res += 8 * num
elif finger == 5:
    res += 4 + 8 * num
else:
    res += 4 * num + 1
    if num % 2 == 0:
        res += finger - 2
    else:
        res += 4 - finger

print(res)