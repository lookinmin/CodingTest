# 키로거, S2, 스택

from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
    arr = list(stdin.readline().rstrip())
    r_list = []
    l_list = []
    # 기본적으로 들어오는 문자는 l에 넣어주면서
    # < 는 왼쪽꺼를 오른쪽에 넣어주고
    # > 는 오른쪽을 왼쪽에 넣어준다
    # - 는 왼쪽에서 문자하나 날린다
    # 오른쪽 스택을 뒤집어서 왼쪽에 붙인다
    for i in arr:
        if i == '-':
            if l_list:
                l_list.pop()
        elif i == '<':
            if l_list:
                r_list.append(l_list.pop())
        elif i == '>':
            if r_list:
                l_list.append(r_list.pop())
        else:
            l_list.append(i)

    l_list.extend(reversed(r_list))

    print(''.join(l_list))