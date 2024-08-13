
def is_on_board(x, y, board):
    # Check if x is within the row boundaries
    if 0 <= x < len(board):
        # Check if y is within the column boundaries
        if 0 <= y < len(board[0]):
            return True
    return False

def safe_set_value(x, y, value, board):
    if is_on_board(x, y, board):
        board[x][y] = value
        return True
    return False