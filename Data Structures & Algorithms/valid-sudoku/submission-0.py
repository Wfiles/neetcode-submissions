class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        rows = defaultdict(set)
        columns = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                box_id = (r//3, c//3)
                if (val in boxes[box_id] or
                    val in rows[r] or
                    val in columns[c]):
                        return False
                boxes[box_id].add(val)
                rows[r].add(val)
                columns[c].add(val)
        return True


        