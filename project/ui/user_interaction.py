def is_name_valid(name):
    return len(name) > 2


def is_board_size_valid(board_size):
    return 1 <= board_size <= 26


def is_number_of_mines_valid(board_size, number_of_mines):
    return 0 < number_of_mines <= board_size*board_size/2


def register_user():
    name = input("Hello,whats your name")
    if not is_name_valid(name):
        print('Your name is too short')
        name = None
    else:
        board_size = int(input(f"{name}, please choose board size"))
        if not is_board_size_valid(board_size):
            print(f"{name}, you have entered illegal board size")
            board_size = None
        else:
            number_of_mines = int(input(f"{name}, for board size " f"{board_size}, choose number of mines to allocate"))
            if not is_number_of_mines_valid(board_size, number_of_mines):
                print(f"{name}, you have entered illegal number of mines")
                number_of_mines = None
            else:
                print(f"{name}, the board size is: " f"{board_size}, number of mines is: " f"{number_of_mines}. ENJOY!")


register_user()




