from sys import stdin
import copy
lst = list(map(int, stdin.readline().split()))

tmp = copy.deepcopy(lst)
if lst == sorted(tmp):
    print('ascending')
elif lst == sorted(tmp, reverse=True):
    print('descending')
else:
    print('mixed')