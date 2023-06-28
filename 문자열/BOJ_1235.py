# 학생 번호, S4, 문자열

from sys import stdin

n = int(stdin.readline())

nums = []
for i in range(n):
    nums.append(stdin.readline().rstrip())

cnt = 1

while 1:
    if len({num[-cnt : ] for num in nums}) == n:
        print(cnt)
        break
    cnt += 1