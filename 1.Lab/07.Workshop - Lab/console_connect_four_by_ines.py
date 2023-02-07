class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


# Print matrix
def print_matrix(ma):
    for el in ma:
        print(el)


def validate_column_choice(selected_column_num, max_column_index):
    # Verify player choice of number of the columns - if not ask again
    if not (0 <= selected_column_num <= max_column_index):
        raise InvalidColumnError


def place_player_choice(ma, selected_column_index, p_num):
    # Place player marker on the spot.
    # Check if the column is full if so - ask throw error.
    row_count = len(ma)
    for row_index in range(row_count - 1, -1, -1):
        current_element = ma[row_index][selected_column_index]
        if current_element == 0:
            ma[row_index][selected_column_index] = p_num
            return row_index, selected_column_index
    raise FullColumnError


def is_player_num(ma, row, col, p_num):
    if col < 0 or row < 0:
        return False
    try:
        if ma[row][col] == p_num:
            return True
    except IndexError:
        return False
    return False


def is_horizontal(ma, row, col, p_num, slots_count):
    count_right = [is_player_num(ma, row, col + index, p_num) for index in range(slots_count)].count(True)
    count_left = [is_player_num(ma, row, col - index, p_num) for index in range(slots_count)].count(True)
    return (count_left + count_right) > slots_count


def is_right_diagonal(ma, row, col, p_num, slots_count):
    right_up_count = [is_player_num(ma, row - index, col + index, p_num) for index in range(slots_count)].count(True)
    left_down_count = [is_player_num(ma, row + index, col - index, p_num) for index in range(slots_count)].count(True)
    return (right_up_count + left_down_count) > 4


def is_left_diagonal(ma, row, col, p_num, slots_count):
    right_down_count = [is_player_num(ma, row+index, col+index, p_num) for index in range(slots_count)].count(True)
    left_up_count = [is_player_num(ma, row-index, col-index, p_num) for index in range(slots_count)].count(True)
    return (right_down_count + left_up_count) > 4


def is_winner(ma, row, col, p_num,  slots_count=4):
    is_down = all([is_player_num(ma, row+index, col, p_num) for index in range(slots_count)])
    if any(
            [
             is_horizontal(ma, row, col, p_num, slots_count),
             is_left_diagonal(ma, row, col, p_num, slots_count),
             is_right_diagonal(ma, row, col, p_num, slots_count),
             is_down
            ]
    ):
        return True
    return False


rows_count = 6
cols_count = 7
# Create matrix
matrix = [[0 for _ in range(cols_count)]for row_num in range(rows_count)]
print_matrix(matrix)

player_num = 1
while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        # Read column choice from input
        colum_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_column_choice(colum_num, cols_count-1)
        row, col = place_player_choice(matrix, colum_num, player_num)
        if is_winner(matrix, row, col, player_num):
            print(f"The winner is player {player_num}")
            print_matrix(matrix)
            break
        print_matrix(matrix)
    except InvalidColumnError:
        print(f"This colum is not valid."
              f"Please select a number between {1} and {cols_count}")
        continue
    except ValueError:
        print("Please select a valid digit!")
        continue
    except FullColumnError:
        print(f"This column is already full! Please select other column number!")
        continue

    player_num += 1

