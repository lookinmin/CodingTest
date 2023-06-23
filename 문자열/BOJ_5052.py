# 전화번호 목록, G4, 문자열-트리

from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline().rstrip())
    arr = []

    for _ in range(n):
        arr.append(stdin.readline().rstrip())

    arr.sort()      # 그냥 정렬하면 prefix 가능성이 있는 번호가 앞뒤로 정렬됨
    # 길이로 정렬하면 안됬음

    flag = True

    for i in range(n-1):
        long = len(arr[i])
        if arr[i] == arr[i+1][:long]:       # 바로 다음거 확인해서 겹치는 부분 있으면 NO
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")