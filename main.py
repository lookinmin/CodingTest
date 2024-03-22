def solution(arr):
    res = {}
    for num in arr:
        res[num] = res.get(num, 0) + 1
    return res


print (solution([3, 1, 4, 2, 3, 1, 5, 6]))
