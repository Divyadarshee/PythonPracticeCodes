# link: https://leetcode.com/problems/valid-sudoku/
# Time: O(n)
# Revision date: 22/1/23
###############----HINTS----####################
# hint: set for each checking features - row, column, sub-board(3X3)
# hint: use key for sub-board as row//3, col//3
# hint: use default dict
# Remember: dictionary can only take tuple as the key and not a list

from typing import List
from collections import defaultdict

class Solution:
    def validSudoku(self, board: List[List[int]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # Key - (row/3, col/3)

        for r in range(9):
            for c in range(9):
                if(board[r][c] == "."):
                    continue
                if(board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True