# 최대값 출력하기

arr = list(map(int, input().split()))
arr = sorted(arr)

res = []
res.append(arr[0] + arr[1] + arr[2])
res.append((arr[0] + arr[1]) * arr[2])
res.append(arr[0] * (arr[1] + arr[2]))
res.append(arr[0] * arr[1] * arr[2])
print(max(res))