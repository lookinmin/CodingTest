# S1, 북극곰은 괄호를 찢어
from sys import stdin

n = int(input())
s = stdin.readline().rstrip()
if len(s) % 2 != 0:
    print(-1)
    exit()

day = 0
min_day = 0

for w in s:
    if w == '(':
        day += 1
    else:
        day -= 1
    if abs(day) > min_day:
        min_day = abs(day)
        
if day == 0:
    print(min_day)
else:
    print(-1)