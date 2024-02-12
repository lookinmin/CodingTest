# S2, 화학식량

words = input().rstrip()

weight = {'H' : 1, 'C' : 12, 'O' : 16}

stack = []

for word in words:
    if word == '(':
        stack.append(word)
    elif word == ')':
        tmp = 0
        while 1:
            if stack[-1] == '(':
                stack.pop()
                stack.append(tmp)
                break
            else:
                tmp += stack.pop()
    elif word in weight.keys():
        stack.append(weight[word])
    else:
        stack.append(stack.pop() * int(word))

print(sum(stack))
