from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(idx):
            nums = set()
            for i in range(9):
                if board[idx][i] != ".":
                    if board[idx][i] in nums:
                        return False
                    nums.add(board[idx][i])
            return True

        def check_col(idx):
            nums = set()
            for i in range(9):
                if board[i][idx] != ".":
                    if board[i][idx] in nums:
                        return False
                    nums.add(board[i][idx])
            return True

        def check_box(x, y):
            nums = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] != ".":
                        if board[i][j] in nums:
                            return False
                        nums.add(board[i][j])
            return True
        
        # Check all rows and columns
        for i in range(9):
            if not check_row(i) or not check_col(i):
                return False
        
        # Check all 3x3 boxes
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                if not check_box(x, y):
                    return False
        
        return True