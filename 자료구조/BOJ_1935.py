# 후위 표기식2, S3, 스택

from sys import stdin

n = int(stdin.readline().rstrip())

arr = list(stdin.readline().rstrip())
val = [0] * n
for i in range(n):
    val[i] = int(stdin.readline().rstrip())

stack = []

for i in arr:
    if 'A' <= i <= 'Z':
        stack.append(val[ord(i) - ord('A')])        # 식에서 알파벳을 만나면 숫자 형식으로 stack에 저장
        # 어차피 알파벳 순서대로 등장하는 인덱스이기 때문에 가능
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)


print("{:.2f}".format(stack[0]))
