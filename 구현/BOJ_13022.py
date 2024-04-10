# 늑대와 올바른 단어, S2
from sys import stdin
words = stdin.readline().rstrip()
from collections import defaultdict

if len(words) % 4 != 0:
    print(0)
    exit()

if words.count('w') != words.count('o'):
    print(0)
    exit()

dic = defaultdict(int)
for c in words:
    if c == 'w':
        dic['w'] += 1
        if dic['o'] > 0 or dic['l'] > 0 or dic['f'] > 0:
            print(0)
            exit()
    elif c == 'o':
        if dic['w'] == 0:
            print(0)
            exit()
        dic['o'] += 1
    elif c == 'l':
        if dic['w'] != dic['o']:
            print(0)
            exit()
        dic['l'] += 1
    else:
        if dic['w'] != dic['o'] or dic['o'] != dic['l']:
            print(0)
            exit()
        dic['f'] += 1

    if len(set(dic.values())) == 1:
        for x in ['w', 'o', 'l', 'f']:
            dic[x] = 0

if len(set(dic.values())) == 1:
    print(1)
else:
    print(0)