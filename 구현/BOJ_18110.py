from sys import stdin
n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(int(stdin.readline().rstrip()))

if n == 0:
    print(0)
    exit()

arr.sort()
k = int((n * 0.15) + 0.5)
arr = arr[k : n-k]
avg = int((sum(arr) / len(arr)) + 0.5)
print(avg)
