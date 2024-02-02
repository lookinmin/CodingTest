from sys import stdin

A, p = map(int, stdin.readline().split())

arr = [A]
idx = 1
while 1:
    num = list(str(arr[idx-1]))
    k = 0
    for n in num:
        k += int(n) ** p
    if k not in arr:
        arr.append(k)
        idx += 1
    else:
        isIn = k
        break

location = arr.index(isIn)
print(location)
