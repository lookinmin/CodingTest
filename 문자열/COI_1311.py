# 저항
from sys import stdin
a = str(stdin.readline().rstrip())
b = str(stdin.readline().rstrip())
c = str(stdin.readline().rstrip())



arr = {'black' : 1,
       'brown' : 10,
       'red' : 100,
       'orange' : 1000,
       'yellow' : 10000,
       'green' : 100000,
       'blue' : 1000000,
       'violet' : 10000000,
       'grey' : 100000000,
       'white' : 1000000000}

tmp = list(arr.keys())
a1 = str(tmp.index(a))
b1 = str(tmp.index(b))
op = int(a1+b1)
val = arr[c]
print(op*val)
