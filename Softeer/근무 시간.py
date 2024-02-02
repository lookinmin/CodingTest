import sys

total = 0
for _ in range(5):
    start, end = sys.stdin.readline().split()
    a_h, a_m = start.split(':')
    e_h, e_m = end.split(':')
    total += ((60*int(e_h) + int(e_m)) - (60*int(a_h) + int(a_m)))

print(total)