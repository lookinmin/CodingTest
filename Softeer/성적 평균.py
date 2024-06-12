from sys import stdin
n, k = map(int, stdin.readline().split())
s = list(map(int, stdin.readline().split()))
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    a -= 1
    b -= 1
    avg = sum(s[a : b + 1]) / len(s[a : b + 1])
    print("{:.2f}".format(avg))