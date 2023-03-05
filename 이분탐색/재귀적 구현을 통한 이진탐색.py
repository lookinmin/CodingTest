def bin_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return bin_search(arr,target, start, mid-1)
    else:
        return bin_search(arr, target, mid+1, end)

n, target = map(int, input().split())
arr = list(map(int, input().split()))

res = bin_search(arr, target, 0, n-1)
if res == None:
    print("NONE")
else:
    print(res + 1)
