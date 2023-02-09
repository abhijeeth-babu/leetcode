class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {num:set() for num in range(10)}
        rows = {num:set() for num in range(10)}
        squares = {(num//3, num % 3): set() for num in range(10)}
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                r_s, c_s = r // 3, c // 3
                if num != ".":
                    if (num in rows[r] or
                        num in cols[c] or
                        num in squares[(r_s, c_s)]):
                        return False
                    cols[c].add(num)
                    rows[r].add(num)
                    squares[(r_s, c_s)].add(num)
        return True
