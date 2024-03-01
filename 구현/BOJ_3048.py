# 개미, S4

from sys import stdin
n1,n2 = map(int, stdin.readline().split())
a = list(stdin.readline().rstrip())[::-1]
b = list(stdin.readline().rstrip())
t = int(stdin.readline())


total = a + b

for _ in range(t):
    for i in range(len(total) - 1):
        if total[i] in a and total[i+1] in b:
            total[i], total[i + 1] = total[i+1], total[i]
            if total[i + 1] == a[-1]:
                break

print("".join(total))