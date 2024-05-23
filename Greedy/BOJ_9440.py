# 숫자 더하기, S2
from sys import stdin
while 1:
    tmp = list(map(int, stdin.readline().split()))
    if tmp[0] == 0:
        exit()
    
    arr = sorted(tmp[1:])
    one = ''
    two = ''

    zeroCount = 0
    flag = True
    
    for num in arr:
        if num == 0:
            zeroCount += 1
            continue
        if flag:
            one += str(num)
            flag = False
        else:
            two += str(num)
            flag = True
    
    for _ in range(zeroCount):
        if len(one) == len(two):
            one = one[0] + '0' + one[1:]
        else:
            two = two[0] + '0' + two[1:]
    
    
    print(eval("{} + {}".format(one, two)))
    