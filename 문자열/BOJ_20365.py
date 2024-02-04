# 블로그2, S3

from sys import stdin

n = int(stdin.readline())
tasks = stdin.readline().rstrip()

toB = ' '.join(tasks.split('R')).split()        # R 기준 나누기
toR = ' '.join(tasks.split('B')).split()        # B 기준 나누기

if len(toB) == 0 or len(toR) == 0:
    print(1)
else:
    print(min(len(toB), len(toR)) + 1)

