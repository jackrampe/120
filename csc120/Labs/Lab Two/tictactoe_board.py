"""Models a tic-tac-toe board.

Authors: Aaron Cass, Kristina Striegnitz
Version: fall 2023
"""

SIZE = 3
EMPTY = ' '

def create(rows=None):
    """Create a tictactoe board with given cell values.  If no initial 
    cell values are given, create an empty tictactoe board.

    Parameters
    ----------
    rows : list
        A list of 3 3-character strings, where each character 
        is either 'X', 'O', or ' '. Each of the 3-character strings 
        represents a row of the tictactoe board.
        
    Returns
    -------
    list
        A tictactoe board with those values, represented as a nested list.
    """
    board = []
    if rows is None:
        empty_row = [EMPTY] * SIZE
        for i in range(SIZE):
            board.append(empty_row)
    else:
        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                row.append(rows[i][j])
            board.append(row)

    return board


def place_piece(board, i, j, piece):
    """Place a piece (either 'X' or 'O') on the board.
:~/CSC120/Week 2/Thu Lab starter code-20230914$ /bin/python "/home/carretea/CSC120/Week 2/Thu Lab starter code-20230914/test_tictactoe_board.py"
Traceback (most recent call last):
  File "/home/carretea/CSC120/Week 2/Thu Lab starter code-20230914/test_tictactoe_board.py", line 7, in <module>
    import tictactoe_board as ttt_board
  File "/home/carretea/CSC120/Week 2/Thu Lab starter code-20230914/tictactoe_board.py", line 81
    row_str += column + ' | 'row
                             ^
    Parameters
    ----------Tuesday: 2:45-3:45pm Note: on Tue, 9/19 office hours will be 2:15-3:15pm instead.
Friday: 10:45-11:45am

In Steinmetz 227.  (Email to set up an appointment if none of the above times work.)

CS
    board : list
        The board to modify
    i : int
        The row in which to place a piece (0, 1, or 2)
    j : int
        The column in which to place a piece (0, 1, or 2)
    piece : str 'X' or 'O' 
        The piece to place.
    """
    board[i][j] = piece


def clear_cell(board, i, j):
    """Clear a cell on the tictactoe board.

    Parameters
    ----------
    board : list
        The board to modify
    i : int
        The row with the cell to clear
    j : int
        The column with the cell to clear
    """
    place_piece(board, i, j, EMPTY)

# bug may be here
def _row_as_string(row):
    row_str = ''
    for column in row[:-1]:
        row_str += column + ' | '
    row_str += row[-1]
    return row_str


def as_string(board):
    """Return a string representation of the given board.
:~/CSC120/Week 2/Thu Lab starter code-20230914$ /bin/python "/home/carretea/CSC120/Week 2/Thu Lab starter code-20230914/test_tictactoe_board.py"
Traceback (most recent call last):
  File "/home/carretea/CSC120/Week 2/Thu Lab starter code-20230914/test_tictactoe_board.py", line 7, in <module>
    import tictactoe_board as ttt_board
  File "/home/carretea/CSC120/Week 2/Thu Lab starter code-20230914/tictactoe_board.py", line 81
    row_str += column + ' | 'row
                             ^
    Parameters
    ----------
    board : list
        The board to show

    Returns
    -------
    str
        The string representation of the board.
    """
    board_str = ''
    for row in board[:-1]:
        board_str += _row_as_string(row)
        board_str += '\n----------\n'
    board_str += _row_as_string(board[-1])
    board_str += '\n'
    return board_str


def show(board):
    """Print the board.

    Parameters
    ----------
    board : list
        The tictactoe board to pr:~/CSC120/Week 2/Thu Lab starter code-20230914$ /bin/python "/home/carretea/CSC120/Week 2/Thu Lab starter code-20230914/test_tictactoe_board.py"
Traceback (most recent call last):
  File "/home/carretea/CSC120/Week 2/Thu Lab starter code-20230914/test_tictactoe_board.py", line 7, in <module>
    import tictactoe_board as ttt_board
  File "/home/carretea/CSC120/Week 2/Thu Lab starter code-20230914/tictactoe_board.py", line 81
    row_str += column + ' | 'row
                             ^int
    """
    print(as_string(board))


def _three_in_row(board, player, start_x, start_y, dx, dy):
    """Determine if a player has three in a row, starting from a 
    starting position (start_x, start_y) and going in the direction 
    indicated by (dx, dy).
    """
    x = start_x
    y = start_y
    for i in range(0, SIZE):
        if board[y][x] != player:
            return False
        x += dx
        y += dy

    return True


def _is_winner(board, player):
    """Return True if and only if the given player has won."""
    if _three_in_row(board, player, 0, 0, 1, 1):
        return True
    elif reverse_diagonal(board,player, 0,2,1,1):
        return True 
    else:
        for i in range(0, SIZE):
            if (_three_in_row(board, player, 0, i, 1, 0)
                or _three_in_row(board, player, i, 0, 0, 1)):
                     True
        return False

def reverse_diagonal(board, player, start_x, start_y, dx, dy):
    '''
    Returns True if player has won via a reverse diagonal 
    Parameter: board: the board
    parameter player: The player being tested
    parameter start_x, start_y; starting coordinates
    parameter dx, dy; direction to look. 
    '''
    x = start_x
    y = start_y
    for i in range(0,SIZE):
        if board[x][y] != player:
            return False
        x+=dx
        y-=dy
    return True 
            
    
def get_winner(board):
    """Determine if there is a winner and return the player who has won.

    Parameters
    ----------
    board : list
        A tictactoe board.
    
    Returns
    -------
    str
        'X' if player X is the winner; 'O' if player O is the winner; 
        None if there is no winner.
    """
    if _is_winner(board, 'X'):
        return 'X'
    elif _is_winner(board, 'O'):
        return 'O'
    else:
        return None
