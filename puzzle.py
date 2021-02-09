"""My solution to problem 2"""
"""https://github.com/booyakashakawabangha/Lab_repository_1"""

board = [\
    "**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"\
    ]


def ten_digits_set():
    """
    This function returns a set of all ten digits.
    """
    digits = '0123456789'
    return set(digits)


def check_uniqueness_in_rows(board: list) -> bool:
    """
    This function checks if all elements in a row are unique.
    Returns True if yes. False - otherwise.
    >>> check_uniqueness_in_rows(["**** ****", "***1 ****", "**  3****"])
    True
    >>> check_uniqueness_in_rows(["**** ****", "***1 ****", "**3 3****"])
    False
    """
    for line in board:
        digit_set = set()
        for elem in line:
            if elem in digit_set:
                return False
            elif elem in ten_digits_set():
                digit_set.add(elem)
    return True


def check_uniqueness_in_columns(board: list) -> bool:
    """
    This function checks if all elements in a column are unique.
    Returns True if yes. False - otherwise.
    >>> check_uniqueness_in_columns(["** ****", "*1 ****", "  3****"])
    True
    >>> check_uniqueness_in_columns(["** ****", "*1 ****", " 13****"])
    False
    """
    reversed_board = list()
    for i in range(len(board)):
        column = str()
        for line in board:
            column += line[i]
        reversed_board.append(column)
    if check_uniqueness_in_rows(reversed_board):
        return True
    return False


def check_uniqueness_by_color(board: list) -> bool:
    """
    This function checks if all elements in a cells of same color \
    are unique.
    Returns True if yes. False - otherwise.
    """
    vert_idx = 0
    for hor_idx in range(8, 3, -1):
        current_color_set = set()
        for elem in board[hor_idx]:
            if elem in current_color_set:
                return False
            if elem in ten_digits_set():
                current_color_set.add(elem)
        board.pop(hor_idx)

        for line in board:
            if line[vert_idx] in current_color_set:
                return False
            if line[vert_idx] in ten_digits_set():
                current_color_set.add(line[vert_idx])

        vert_idx += 1
    return True


def validate_board(board: list) -> bool:
    """
    This function returns True if a board satisfies next demands:
    1) All numbers in a row are unique;
    2) All numbers in a column are unique;
    3) All numbers in the same color are unique.
    False - otherwise.
    """
    if check_uniqueness_in_rows(board) and \
       check_uniqueness_in_columns(board) and \
       check_uniqueness_by_color(board):
        return True
    return False


if __name__ == "__main__":
    print(validate_board(board))
