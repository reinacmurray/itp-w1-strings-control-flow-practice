BOARD_TEMPLATE = """
{0}  |  {1}  |  {2}
--------------
{3}  |  {4}  |  {5}
--------------
{6}  |  {7}  |  {8}
"""

def format_tic_tac_toe_board(first_row, second_row, third_row):
    return BOARD_TEMPLATE.format(
        first_row[0], first_row[1], first_row[2],
        second_row[0], second_row[1], second_row[2],
        third_row[0], third_row[1], third_row[2],
    )


def test_format_board():
    """
    This is the board used in this test:

        X  |  O  |  X
        --------------
        O  |  X  |  O
        --------------
        O  |  O  |  X

    """
    first_row = 'XOX'
    second_row = 'OXO'
    third_row = 'OOX'
    expected_board = """
X  |  O  |  X
--------------
O  |  X  |  O
--------------
O  |  O  |  X
"""
    board = format_tic_tac_toe_board(first_row, second_row, third_row)

    assert board == expected_board
