# 도서관, G5, 그리디

from sys import stdin

n,m = map(int, stdin.readline().split())
books = list(map(int,stdin.readline().split()))
neg_books = []
pos_books = []

for book in books:
    if book < 0:
        neg_books.append(book)
    else:
        pos_books.append(book)

neg_books.sort()
pos_books.sort(reverse=True)

distance = []

for i in range(len(neg_books) // m):
    distance.append(abs(neg_books[m*i]))
if len(neg_books) % m > 0:
    distance.append(abs(neg_books[(len(neg_books)//m)*m]))

for i in range(len(pos_books) // m):
    distance.append(abs(pos_books[m*i]))
if len(pos_books) % m > 0:
    distance.append(abs(pos_books[(len(pos_books)//m)*m]))

distance.sort()
res = distance.pop()
res += 2 * sum(distance)
print(res)