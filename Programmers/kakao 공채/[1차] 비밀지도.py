def solution(n, arr1, arr2):
    answer = [[' '] * n for _ in range(n)]

    board1 = []
    board2 = []

    for num in arr1:
        bi = format(num, 'b')
        bi = bi.zfill(n)
        # 출처 : https://dojang.io/mod/page/view.php?id=2300
        board1.append(bi)
    for num in arr2:
        bi = format(num, 'b')
        bi = bi.zfill(n)
        board2.append(bi)

    print(board1)
    print(board2)

    for i in range(n):
        for j in range(n):
            if board1[i][j] == '0' and board2[i][j] == '0':
                answer[i][j] = ' '
            else:
                answer[i][j] = '#'

    res = []
    for line in answer:
        tmp = ''
        for i in line:
            tmp += i
        res.append(tmp)

    return res