def solution(mats, park):
    # 지민이의 돗자리는 정사각형
    sorted_mats = sorted(mats, reverse = True)
    # 돗자리 길이가 긴 순서대로
    
    n = len(park)
    m = len(park[0])
    
    # 최대 20 * (50 * 50) * (10 * 10)
    for mat in sorted_mats:
        for i in range(n):
            for j in range(m):
                if park[i][j] == '-1':
                    flag = True
                    for k in range(mat):
                        for l in range(mat):
                            if i + k <= n-1 and j + l <= m-1:
                                if park[i + k][j + l] != '-1':
                                    flag = False
                                    break
                            else:
                                flag = False
                                break      
                        if flag == False:
                            break
                    if flag:
                        return mat
    return -1