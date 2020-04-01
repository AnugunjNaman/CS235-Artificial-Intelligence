

def valid_sticks_check(original_number_of_sticks):
    if original_number_of_sticks < 5 or original_number_of_sticks > 100:
        print("Please select a number between 10 and 100")
        return False
    else:
        return True

def no_sticks_left(total_sticks_left):
    if total_sticks_left < 1:
        return True
    else:
        return False

def input_sticks():
    while True:
        n = eval(input('Enter number of sticks: '))
        if valid_sticks_check(n):
            return n

def valid_input_player(input_player):
    if input_player < 1 or input_player > 3:
        print("Out of range! Please enter a number between 1 and 3.")
        return False
    else:
        return True

def player_takes_out_sticks(player):
    while True:
        player_input = int(input("Player {}: How many sticks do you take (1-3)? ".format(player)))
        if valid_input_player(player_input):
            return player_input

def update_num_sticks(sticks_left, player_sticks):
    while True:
        if valid_input_player(player_sticks) and player_sticks <= sticks_left:
            sticks_left -= player_sticks
            return sticks_left
        else:
            print("You can't take more than there is left!")
            print("There are {} sticks left.".format(sticks_left))
            player_sticks = int(input("Please enter a valid input: "))

def two_players_game(original_number_sticks):
    total_sticks_left = original_number_sticks

    while True:
        first_player_sticks = player_takes_out_sticks('1')
        total_sticks_left = update_num_sticks(total_sticks_left, first_player_sticks)
        print("There are {} sticks left".format(total_sticks_left))

        if no_sticks_left(total_sticks_left):
            print("Player 1, you lose.")
            break

        second_player_sticks = player_takes_out_sticks('2')
        total_sticks_left = update_num_sticks(total_sticks_left, second_player_sticks)
        print("There are {} sticks left.".format(total_sticks_left))

        if no_sticks_left(total_sticks_left):
            print("Player 2, you lose.")
            break

def main():
    print("Welcome to the Game of Sticks!")

    while True:
        num_sticks = input_sticks()
        two_players_game(num_sticks)

        repeat = input("Would you like to play again? y/n: ").lower()
        if repeat == 'y':
            continue
        else:
            break

if __name__ == '__main__':
    main()