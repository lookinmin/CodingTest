# 폴리오미노, S5, 구현

board = input()

idx = 0
newboard = ''

while idx<len(board):
    if board[idx:idx+4]=='XXXX':
        newboard += 'AAAA'
        idx += 4
    elif board[idx:idx+2]=='XX':
        newboard +='BB'
        idx += 2
    elif board[idx]=='X':
        newboard = -1
        break
    else :
        newboard += board[idx]
        idx += 1

print(newboard)

# board = input()
#
# board = board.replace('XXXX', 'AAAA')
# board = board.replace('XX', 'BB')
#
# if 'X' in board: print(-1)
# else: print(board)