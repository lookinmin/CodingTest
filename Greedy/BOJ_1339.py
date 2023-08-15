# 단어 수학, G4, 그리디

from sys import stdin

# GCF + ACDEB = 783 + 98654

n = int(stdin.readline())
words = []

for _ in range(n):
    words.append(list(stdin.readline().rstrip()))

mapping = dict()

res = 0


for word in words:
    k = len(word) - 1           # 5자리수 라면 10^4 = 10000 값
    for w in word:
        if w in mapping:
            mapping[w] += (10**k)
        else:
            mapping[w] = (10**k)
        k -= 1

mapping = sorted(mapping.values(), reverse=True)

res, m = 0, 9

for value in mapping:
    res += value * m
    m -= 1

print(res)
