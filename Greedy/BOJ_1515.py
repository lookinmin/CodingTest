# 수 이어쓰기, S3, 구현-그리디

from sys import stdin

A = stdin.readline().rstrip()

# 1부터 수를 증가시키며 A의 숫자들이 하나씩 나올때까지 증가시키며 찾는다

num = 0

while 1:
    num += 1
    s = str(num)

    while len(s) > 0 and len(A) > 0:
        if s[0] == A[0]:        # 맨앞에꺼 일치하면 지운다
            A = A[1:]
        s = s[1:]

    if A == '':
        print(num)
        break
