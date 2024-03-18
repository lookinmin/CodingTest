# 다음수 구하기, S2
from sys import stdin
T = int(stdin.readline())

for _ in range(T):
    data = list(map(int, list(stdin.readline().rstrip())))

    k, idx = len(data), 0

    for i in range(k-1, 0, -1):
        if data[i] > data[i - 1]:
            if i == k - 1:
                idx = k - 2
            else:
                idx = i - 1
            break

    a = data[:idx]
    b = data[idx:]

    if not a or not b:
        print("BIGGEST")
    else:
        b.sort()
        for i in range(len(b)):
            if b[i] > data[idx]:
                a.append(b.pop(i))
                a.extend(b)
                break
        print(''.join(map(str, a)))