# 파일정리, S3, 문자열

from sys import stdin

n = int(stdin.readline())

files = dict()

for _ in range(n):
    tmp = (stdin.readline().split('.')[1])
    if not tmp in files:
        files[tmp] = 1
    else:
        files[tmp] += 1

sort_file = sorted(files.items())

for key, value in sort_file:
    print(key.rstrip(), value)
