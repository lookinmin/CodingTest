def solution(n, m, board):
    # 높이 n, 폭 m
    board = [list(row) for row in board]
    answer = 0
    
    while True:
        erase_idx = set()  # 지워질 인덱스를 저장하는 set
        
        # 2x2 블록을 찾기
        for i in range(n - 1):
            for j in range(m - 1):
                # 2x2 블록이 모두 동일한 문자일 경우
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] and board[i][j] != '-1':
                    erase_idx.add((i, j))
                    erase_idx.add((i+1, j))
                    erase_idx.add((i, j+1))
                    erase_idx.add((i+1, j+1))
        
        # 지워질 블록이 없으면 종료
        if not erase_idx:
            break
        
        # 지워진 블록 개수만큼 카운팅
        answer += len(erase_idx)
        
        # 지워질 블록을 모두 '-1'로 설정
        for i, j in erase_idx:
            board[i][j] = '-1'
        
        # 블록을 아래로 떨어뜨리기
        for j in range(m):
            stack = []
            # 현재 열에서 남아 있는 블록들을 스택에 추가
            for i in range(n):
                if board[i][j] != '-1':
                    stack.append(board[i][j])
            
            # 스택에서 꺼내면서 블록을 아래로 떨어뜨리기
            for i in range(n - 1, -1, -1):
                if stack:
                    board[i][j] = stack.pop()  # 스택에서 꺼내서 채움
                else:
                    board[i][j] = '-1'  # 남은 칸은 '-1'로 채움
    
    return answer
