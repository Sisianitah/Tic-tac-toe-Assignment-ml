# tic_tac_tic.py
# Write a simple rule/knowledge-based AI to play tic-tac-toe. All you need to do is give me a single function called play(). Play will recieve a single array of strings of length 9 that contains either an x, an o or an empty string ''. The mapping of the board to the array is as follows:
# |0|1|2|
# |3|4|5|
# |6|7|8|


# So an array like ['', 'x', 'x', 'o', '', '', '', '', ''] maps to a board that looks like so:
# | |X|X|
# |O| | |
# | | | |


# It also means that it is O's turn to play.

# Your play() method will receive this argument and must return a single number (from 0 to 8) representing the next square to be filled with either an X or an O. Of course, it should be obvious which one should come next.

# Remember:
# The first move is an X
# You can only place on vacant squares
# Placing on an already occupied square is illegal
# An illegal move will result in a loss
# The winner is the first to line up Os or Xs horizontally, vertically or diagonally

# An example of a play() function:
# def play(board):
#     # Write your code here
#     if not ('x' in board or 'o' in board):
#         return 4
#     return 3
 
# Submit a link to your code in this thread. Do it in a github repo so I can automate the game later.
# I will give further instructions on how to structure your code so it will participate in the tournament. 


def play(board):
    # Determine whose turn it is
    x_count = board.count('x')
    o_count = board.count('o')
    turn = 'x' if x_count == o_count else 'o'
    opponent = 'o' if turn == 'x' else 'x'

    # All winning combinations
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # 1. Win if possible
    for a, b, c in wins:
        line = [board[a], board[b], board[c]]
        if line.count(turn) == 2 and line.count('') == 1:
            return [a, b, c][line.index('')]

    # 2. Block opponent's win
    for a, b, c in wins:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count('') == 1:
            return [a, b, c][line.index('')]

    # 3. Take center
    if board[4] == '':
        return 4

    # 4. Take a corner
    for i in [0, 2, 6, 8]:
        if board[i] == '':
            return i

    # 5. Take any side
    for i in [1, 3, 5, 7]:
        if board[i] == '':
            return i

    # No move (should not happen if board is valid)
    return -1
