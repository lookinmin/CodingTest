# 한국이 그리울 땐 서버에 접속하지, S3, 문자열

from sys import stdin

# 패턴에 있는 별표를 임의의 문자열로 변환

n = int(stdin.readline().rstrip())

pattern = list(stdin.readline().rstrip())

loca = pattern.index('*')
s = pattern[:loca]
e = pattern[loca+1 : ]

sk = len(s)
ek = len(e)

length = sk + ek


for _ in range(n):
    sample = list(stdin.readline().rstrip())
    if length > len(sample):
        print("NE")
    else:
        if sample[:sk] == s and sample[-ek:] == e:
            print("DA")
        else:
            print("NE")