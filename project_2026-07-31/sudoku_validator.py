def is_valid_sudoku(board: list[list[str]]) -> bool:
    """
    Validates a 9x9 Sudoku board.
    The board is valid if each row, each column, and each of the nine 3x3 subgrids
    contains the digits 1-9 without repetition. Empty cells are represented by ".".
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue

            # Check row
            if val in rows[r]:
                return False
            rows[r].add(val)

            # Check col
            if val in cols[c]:
                return False
            cols[c].add(val)

            # Check subgrid
            subgrid_idx = (r // 3) * 3 + (c // 3)
            if val in subgrids[subgrid_idx]:
                return False
            subgrids[subgrid_idx].add(val)

    return True
