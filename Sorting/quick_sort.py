

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    print("PIVOT", pivot)
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    print("작은것들",lesser_arr)
    print("큰 것들", greater_arr)
    print("------------------------one END--------------------------")
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

print(quick_sort([30, 20, 40, 35, 5, 10, 45, 50, 25, 15]))