# 올바른 괄호 문자열, 중급
# 스택

from sys import stdin

arr = list(stdin.readline().rstrip())
st = []

for i in arr:
    if i == '(':
        st.append(i)
    else:
        if st:
            st.pop()
        else:
            print("bad")
            exit(0)

if len(st) == 0:
    print("good")
else:
    print(len(st))
