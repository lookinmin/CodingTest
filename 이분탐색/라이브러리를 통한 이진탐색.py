# 이진 탐색 라이브러리

from bisect import bisect_left, bisect_right

# bisect_left(arr, x) : 정렬 순서를 유지하며 arr에 x를 삽입할 가장 왼쪽 인덱스
# bisect_right(arr, x) : 정렬 순서를 유지하며 arr에 x를 삽입할 가장 오른쪽 인덱스

# 예) 값이 특정 범위에 속하는 데이터 개수 구하기

def count(arr, left, right):
    right_index = bisect_right(arr, right)
    left_index = bisect_left(arr, left)
    res = right_index - left_index
    return res

arr = [1,2,3,3,3,3,4,5,8,9]

print(count(arr, 2, 5))         # 값이 2~5인 데이터 개수 출력
# 2랑, 5 포함
