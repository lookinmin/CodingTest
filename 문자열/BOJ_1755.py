# 숫자놀이, S4, 문자열

m, n = map(int, input().split())

nums = {'0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six',
        '7' : 'seven', '8' : 'eight', '9' : 'nine'}

arr = []
for i in range(m, n+1):
    si = ''.join([nums[c] for c in str(i)])
    arr.append([i, si])         # 8, eight 이런식으로 저장

arr.sort(key=lambda x : x[1])

for i in range(len(arr)):
    if i % 10 == 0 and i != 0:
        print()
    print(arr[i][0], end = ' ')
