# Fly me to the Alpha Centauri, G5, 수학

from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    x, y = map(int, stdin.readline().split())
    dest = y - x
    # x ~ dest까지
    n = 0
    while 1:
        if dest <= n*(n+1):
            break
        n += 1

    if dest <= n**2:
        print(n*2-1)
    else:
        print(n*2)


