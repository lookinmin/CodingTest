from sys import stdin

n = int(stdin.readline())
res = []
for _ in range(n):
    s, t = map(str, stdin.readline().split())
    # x or X가 등장하는 위치
    s = s.upper()
    idx = s.find('X')
    res.append(t[idx].upper()) 

print(''.join(res))