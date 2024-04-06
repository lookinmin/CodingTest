def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    res = []

    for i in range(row_begin, row_end + 1):
        tmp = data[i - 1]
        val = 0
        for j in range(len(tmp)):
            val += tmp[j] % i
        res.append(val)

    ans = res[0]
    for num in res[1:]:
        ans = ans ^ num
    return ans