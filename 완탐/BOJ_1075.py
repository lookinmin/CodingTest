# B2, 나누기
n = input()
f = int(input())
cvtN = list(map(int, n))

cvtN.pop()
cvtN.pop()
cvtN.append(0)
cvtN.append(0)

num =int(''.join(map(str, cvtN)))

for i in range(0, 100):
    if num % f == 0:
        break
    num += 1


toL = list(map(int, str(num)))[-2:]
res = ''.join(map(str, toL))
print(res)