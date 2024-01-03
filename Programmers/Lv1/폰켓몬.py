def solution(nums):
    N = len(nums) // 2
    uniq = list(set(nums))
    return min(len(uniq), N)