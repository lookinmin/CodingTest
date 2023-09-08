# LCD Test, S2, 문자열

from sys import stdin

s, n = map(int, stdin.readline().split())

n = str(n)

h = '-'
v = '|'


def makenum(n):
    lcd = [[' '] * (s + 2) for _ in range(2 * s + 3)]
    for i in range(1, s + 1):
        if n in '02356789':
            lcd[0][i] = h  # a
        if n in '01234789':
            lcd[i][-1] = v  # b
        if n in '013456789':
            lcd[s + 1 + i][-1] = v  # c
        if n in '0235689':
            lcd[2 * s + 2][i] = h  # d
        if n in '0268':
            lcd[s + 1 + i][0] = v  # e
        if n in '045689':
            lcd[i][0] = v  # f
        if n in '2345689':
            lcd[s + 1][i] = h  # g
    return lcd

display = [makenum(i) for i in n]

for line in zip(*display):
    for r in line:
        print(''.join(r), end=' ')
    print()