# B1, 적어도 대부분의 배수

from sys import stdin

arr = sorted(list(map(int, stdin.readline().split())))

num = arr[2]

while 1:
    cnt = 0
    for i in range(5):
        if num % arr[i] == 0:
            cnt += 1
    if cnt >= 3:
        print(num)
        exit()
    else:
        num += 1