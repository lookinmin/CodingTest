# S1, 민겸 수
minkum = input().rstrip()
minValue = ""
maxValue = ""

cnt = 0
for w in minkum:
    if w == 'M':
        cnt += 1
    else:
        if cnt == 0:
            minValue += '5'
            maxValue += '5'
            continue
        else:
            # 앞에 n개의 M이 있고 K로 끝남
            
            maxtmp = 5 * (10**cnt)
            mintmp = 10**(cnt - 1)

            minValue += str(mintmp)
            minValue += '5'
            
            maxValue += str(maxtmp)
        
            cnt = 0

if cnt > 0:
    maxtmp = '1' * cnt
    mintmp = 10**(cnt - 1)

    maxValue += str(maxtmp)
    minValue += str(mintmp)

print(maxValue)
print(minValue)