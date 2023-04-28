# 싸이버개강총회, S2, 구현

from sys import stdin
s, e, q = map(list, stdin.readline().split())

members = set()
res = 0

start = int(s[0] + s[1] + s[3] + s[4])
end = int(e[0] + e[1] + e[3] + e[4])
qualify = int(q[0] + q[1] + q[3] + q[4])

while 1:
    try:
        t, name = map(str, stdin.readline().split())
        time = int(t[0] + t[1] + t[3] + t[4])
        if time <= start:
            members.add(name)

        elif end <= time <= qualify and name in members:
            members.remove(name)
            res += 1
    except:
        break


print(res)