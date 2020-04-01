from random import randrange

#Checks amount of sticks within the suitable range of play
def valid_sticks_check(original_number_sticks):
    if original_number_sticks < 5 or original_number_sticks > 50:
        print("Out of range! Please enter a number between 5 and 50.")
        return False
    else:
        return True

#Takes input and check whether vaild or not?
def amount_of_sticks_input():
    while True:
        original_number_sticks = int(input("Please input the number of sticks "+
                                            "within the range of (10 - 100): "))

        if valid_sticks_check(original_number_sticks):
            return original_number_sticks

#Check validity of player's move
def valid_input_from_player(player_input):
    if player_input < 1 or player_input > 3:
        print("Out of range! Please enter a number between 1 and 3.")
        return False
    else:
        return True

#Move by player
def player_takes_out_sticks(player):
    while True:
        player_input = int(input("Player {}: How many sticks do you take (1-3)? ".format(player)))

        if valid_input_from_player(player_input):
            return player_input

#Update of sticks
def update_num_sticks(sticks_left, player_sticks):
    while True:
        if valid_input_from_player(player_sticks) and player_sticks <= sticks_left:
            sticks_left -= player_sticks
            return sticks_left
        else:
            print("You can't take more than there is left!")
            print("There are {} sticks left.".format(sticks_left))
            player_sticks = int(input("Please enter a valid input: "))

#Check if sticks are left or not
def no_sticks_left(total_sticks_left):
    if total_sticks_left < 1:
        return True
    else:
        return False

#Intialization of List
def init_ai_list(original_number_sticks):
    ai_list = []
    for index in range(1, original_number_sticks):
        tup = (index, [1, 2, 3], [])
        ai_list.append(tup)
    return ai_list

#Movement of AI
def ai_takes_out_sticks(ai_list, sticks_left):
    tup = ai_list[sticks_left - 1]
    content = tup[1]
    beside = tup[2]

    random_index = randrange(0, len(content))

    random_choice = content[random_index]
    print("AI selects {}".format(random_choice))

    content.pop(random_index)
    beside.append(random_choice)

    tup_updated = (tup[0], content, beside)
    ai_list[sticks_left - 1] = tup_updated
    # print("ai_list", *ai_list, sep='\n')
    return (ai_list, random_choice)


# This function updates the ai_list when the AI wins.
def update_win_ai_list(ai_list):
    updated_ai_list = ai_list

    for item in range(len(updated_ai_list)):
        tup = updated_ai_list[item]
        content = tup[1]
        beside = tup[2]
        if beside != []:
            content.append(beside[0])
            content.append(beside[0])
            beside.pop(0)
    # print("updated_ai_list after: ", *updated_ai_list, sep='\n')
    return updated_ai_list


# This function updates the ai_list when the AI looses.
def update_loose_ai_list(ai_list):
    updated_ai_list = ai_list

    for item in range(len(updated_ai_list)):
        tup = updated_ai_list[item]
        content = tup[1]
        beside = tup[2]

        if beside != []:
            if beside[0] not in content:
                content.append(beside[0])
            beside.pop(0)

    # print("updated_ai_list after: ", *updated_ai_list, sep='\n')
    return updated_ai_list

#Player vs AI
def player_vs_ai_game(original_number_sticks, hat_list):
    total_sticks_left = original_number_sticks
    ai_list = hat_list

    while True:
        player_sticks = player_takes_out_sticks('human')
        total_sticks_left = update_num_sticks(total_sticks_left, player_sticks)
        print("There are {} sticks left".format(total_sticks_left))

        if no_sticks_left(total_sticks_left):
            print("Human, you lose.")
            # print("ai_list after human lost: ", *ai_list, sep='\n')
            return update_win_ai_list(ai_list)

        # This function returns (updated_ai_list, ai_takes_sticks)
        ai_return = ai_takes_out_sticks(ai_list, total_sticks_left)
        total_sticks_left -= ai_return[1]
        print("There are {} sticks left.".format(total_sticks_left))

        if no_sticks_left(total_sticks_left):
            print("AI, you lose.")
            # print("ai_list after AI lost: ", *ai_return[0], sep='\n')
            return update_loose_ai_list(ai_return[0])

def main():
    print("Welcome to the Game of Sticks!")
    num_sticks = amount_of_sticks_input()
    ai_hat_list = init_ai_list(num_sticks)
    while True:
        ai_hat_list = player_vs_ai_game(num_sticks, ai_hat_list)
        repeat = input("Would you like to play again? y/n: ").lower()
        if repeat == 'y':
            continue
        else:
            break


if __name__ == '__main__':
    main()