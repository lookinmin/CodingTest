# 암호출력


one = input().rstrip()
two = input().rstrip()
a = 0

for i in two:
    a += ord(i)

print("{}{}{}{}{}".format(one, chr(a % 15+33),chr(a%10+48),chr(a%26+65),chr(122-a%26)))