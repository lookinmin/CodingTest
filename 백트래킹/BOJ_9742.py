# 순열, S3
from sys import stdin
from math import factorial

def dfs(now, depth):
    global cnt
    if depth == len(arr):
        cnt += 1
        if cnt == num:
            return now

    else:
        for w in arr:
            if w not in now:
                res = dfs(now + w, depth + 1)
                if res:
                    return res
    return

while 1:
    try:
        arr, num = stdin.readline().split()
        num = int(num)
        cnt = 0

        if factorial(len(arr)) < num:
            print(arr, num, '=', 'No permutation')
        else:
            print(arr, num, '=', dfs('', 0))

    except:
        exit()