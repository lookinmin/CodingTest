# GPT-4
def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    res = []
    k -= 1

    while n > 0:
        n -= 1
        fact = 1

        for i in range(1, n + 1):
            fact *= i

        idx = k // fact
        k %= fact

        res.append(arr.pop(idx))

    return res
