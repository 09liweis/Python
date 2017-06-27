# Code for working with crossword puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *Task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name:
# MarkUs Login:
#


def is_empty(c):
    ''' Please complete the docstring for this function
    '''
    return (c == ' ') or (len(c) == 0)

def char_left(row, col):
    ''' (int, int) -> str
        row: row number, an integer from 0 to height-1
        col: column number, an integer from 0 to width-1
        returns: the puzzle character to the left of (row, col)
                 or "" if col == 0
        >>> char_left(0, 0)
        ''
        >>> char_left(0, 1)
        'p'
    '''
    if col == 0:
        return ''
    else:
        return puzzle[row][col-1]
    
def char_right(row, col):
    ''' Please complete the docstring, including a few doctests for this function.
    '''
    if col == width:
        return ''
    else:
        return puzzle[row][col+1]
    
def char_above(row, col):
    ''' Please complete the docstring, including a few doctests for this function.
    '''
    if row == 0:
        return ''
    else:
        return puzzle[row-1][col]
    
def char_below(row, col):
    ''' Please complete the docstring, including a few doctests for this function.
    '''
    if row == height:
        return ''
    else:
        return puzzle[row+1][col]

# When coding the functions below, make sure to use the functions defined above!    
def fit_char_horizontal(row, col, c):
    ''' (int, int, str) -> bool
        row: row number, from 0 to height-1
        col: column number, from 0 to width-1
        c: a character, different from space and also non-empty
        returns: True, if c fits into puzzle horizontally
                 Otherwise False.
        >>> fit_char_horizontal(2, 2, "s")
        True
        >>> fit_char_horizontal(2, 2, "t")
        False
        >>> fit_char_horizontal(2, 3, "t")
        True
    '''    
    return is_empty(char_left(row, col)) and is_empty(char_right(row, col))

def fit_char_vertical(row, col, c):
    ''' (int, int, str) -> bool
        row: row number, from 0 to height-1
        col: column number, from 0 to width-1
        c: a character, different from space and also non-empty
        returns: True, if c fits into puzzle vertically
                 Otherwise False.
        >>> fit_char_vertical(1, 6, "i")
        True
        >>> fit_char_vertical(2, 6, "t")
        False
        >>> fit_char_vertical(2, 6, "n")
        True
    '''    
    pass # Task 7: replace this line with your code
                
def fit_word_horizontal(row, col, word):
    ''' (int, int, str) -> bool
        row: row number, from 0 to height-1
        col: column number, from 0 to width-1
        returns: True if word fits in the puzzle horizontally,
        starting from the position (row, col)
    '''
    lenw = len(word)
    if not is_empty(char_left(row, col)):
        return False
    if not is_empty(char_right(row, col+lenw-1)): # this is the changed line
        return False
    for c in word:
        if col > width-1:
            return False
        if not fit_char_horizontal(row, col, c):
            return False
        col = col + 1
    return True

def fit_word_vertical(row, col, word):
    ''' (int, int, str) -> bool
        row: row number, from 0 to height-1
        col: column number, from 0 to width-1
        returns: True if word fits in the puzzle vertically,
        starting from the position (row, col)
    '''
    lenw = len(word)
    if not is_empty(char_above(row, col)):
        return False
    if not is_empty(char_below(row+lenw-1, col)): # this is the changed line
        return False
    for c in word:
        if row > height-1:
            return False
        if not fit_char_vertical(row, col, c):
            return False
        row = row + 1
    return True
    
    
def put_word(word, row, col, direction):
    ''' (str, int, int, str) -> NoneType
        Adds word to the puzzle starting from (row, col) in 
        the given direction
    '''
    for c in word:
        # Write the line of code that places the character c
        # to the (row, col) position in the puzzle
        # Hint: Use slice operator
        pass # Task 8: remove this line and write your code
        if direction == "H":
            pass # Task 9: remove this line and write your code
            # Set the variable col to the value of the next available column
            # using the appropriate function call
        else:
            pass # Task 10: remove this line and write your code
            # Set the variable row to the value of the next available row
            # using the appropriate function call


def next_col(x):
    ''' (int) -> int
        returns next column to the column x
    '''
    if x < width-1:
        x = x + 1
    return x

def next_row(y):
    ''' (int) -> int
        returns next row to the row y
    '''
    if y < height-1:
        y = y + 1
    return y

def draw_puzzle():
    ''' () -> str
    '''
    result = ''
    for row in range(height):
        result = result + puzzle[row] + "\n"
    return result

# Please note the values below have been provided as samples.
# Feel free to change them as you wish in order to properly test your code.
puzzle = ['python    ', '  e   i   ', '  string  ', '  t   t   ']
width = 10
height = 4          

if __name__ == "__main__": 
    # print(is_empty('c'))
    print(draw_puzzle())
    print(char_left(0, 1))
    print(fit_char_horizontal(2, 2, "s"))
    print(fit_char_horizontal(2, 2, "t"))
    # import doctest
    # doctest.testmod()