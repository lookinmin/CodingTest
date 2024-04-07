def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    k = len(sticker)

    dp1 = [0] * k  # 첫장 포함
    dp2 = [0] * k  # 첫장 미포함

    dp1[0], dp1[1] = sticker[0], max(sticker[0], sticker[1])

    for i in range(2, k - 1):  # 첫장을 포함했으므로 마지막 장은 포함할 수 없음
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, k):
        dp2[i] = max(sticker[i] + dp2[i - 2], dp2[i - 1])

    return max(max(dp1), max(dp2))