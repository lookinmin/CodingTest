# 도어맨, S2, 구현

from sys import stdin

x = int(stdin.readline())
line = list(map(str, stdin.readline().rstrip()))

men = 0
women = 0

for i in range(len(line)):
    if abs(men - women) < x:
        if line[i] == 'M': men += 1
        else: women += 1

    else:
        if line[i] == 'M':
            if abs(men + 1 - women) < x:
                men += 1
            else:
                if i + 1 < len(line) and line[i + 1]== 'W':
                    line[i], line[i+1] = line[i + 1], line[i]
                    women += 1
                else:
                    break
        else:
            if abs(women + 1 - men) < x:
                women += 1
            else:
                if i + 1 < len(line) and line[i + 1]== 'M':
                    line[i], line[i+1] = line[i + 1], line[i]
                    men += 1
                else:
                    break

print(men + women)