# 같이 탄 놀이기구 수

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
cnt = 0
for i in arr:
    for j in arr2:
        if i == j:
            cnt += 1
            continue


print(cnt)