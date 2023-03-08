# 단어 맞추기, S1, 문자열
from sys import stdin

T = int(stdin.readline())

def next_permutation(arr):
    i = len(arr) - 2
    while i>=0 and arr[i] >= arr[i+1]:          # 끝에서부터 비교해 앞 인덱스가 더 작은 곳을 i
        i -= 1
    if i == -1:
        return False

    j = len(arr) - 1
    while arr[i] >= arr[j]:                     # 끝에서 부터 i보다 큰 값을 찾아 j로 정함
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]             # i <-> j Swap
    res = arr[:i + 1]                           # i뒤에 있는 것들의 순서를 뒤집어 줌
    res.extend(list(reversed(arr[i+1:])))
    return res

for _ in range(T):
    strs = list(stdin.readline().rstrip())
    ans = next_permutation(strs)
    if not ans:
        print("".join(strs))
    else:
        print("".join(ans))