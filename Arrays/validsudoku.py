#Problem No. 36 - Valid Sudoku
class Solution(object):
    def isValidSudoku(self, board):

        for row in board:
            nums = [x for x in row if x != '.']
            if len(nums) != len(set(nums)):
                    return False


        for c in range(9):
            col = []
            for r in range(9):
                if board[r][c] != '.':
                    col.append(board[r][c])

            if len(col) != len(set(col)):
                return False


        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                box = []

                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        if board[r][c] != '.':
                            box.append(board[r][c])

                if len(box) != len(set(box)):
                    return False

        return True