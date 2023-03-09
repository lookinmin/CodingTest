# 층간소음2
from sys import stdin
arr = list(map(int,stdin.readline().split()))

tmp = sum(arr) / 5

for i in arr:
    if i >= 57:
        print("loud")
        exit(0)

if tmp >= 43:
    print("loud")
elif 30 <= tmp < 43:
    print("normal")
else:
    print("silent")