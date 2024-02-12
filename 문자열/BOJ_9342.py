from sys import stdin
import re

T = int(stdin.readline())

check = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(T):
    words = stdin.readline().rstrip()
    if check.match(words) == None:
        print("Good")
    else:
        print("Infected!")