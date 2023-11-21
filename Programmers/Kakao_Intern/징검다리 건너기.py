def solution(stones, k):
    s = 1
    e = max(stones)

    while s <= e:
        mid = (s + e) // 2
        cnt = 0

        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
                if cnt == k:
                    break

            else:
                cnt = 0
        if cnt < k:
            s = mid + 1
        else:
            e = mid - 1

    return s