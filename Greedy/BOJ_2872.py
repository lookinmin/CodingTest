# 우리집엔 도서관이 있어, S2
from sys import stdin

n = int(stdin.readline())
books = []
res = 0
last = 0
for _ in range(n):
    book = int(stdin.readline())
    if book > last:
        last = book
    else:
        res = max(res, book)

print(res)