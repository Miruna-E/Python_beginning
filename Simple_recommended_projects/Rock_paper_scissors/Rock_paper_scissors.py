global game_ongoing
game_ongoing = 1

def won(winner):
    print(winner, "won!")
    global game_ongoing
    game_ongoing = 0
    return

#made a tuple instead of a list so searching is done faster. options don't change during running
#options is made to be ordered
options = ("paper", "scissors", "rock",)
options_length = len(options)

while(game_ongoing):
    user_choice = input("Chose between \"rock\", \"paper\" and \"scissors\"\n")
    while(user_choice not in options):
        user_choice = input("Chose between \"rock\", \"paper\" and \"scissors\"\n")

    user_won = 1

    from random import randrange
    computer_choice_options_index = randrange(options_length)
    computer_choice = options[computer_choice_options_index]
    print("Computer chose", computer_choice)

    # 0 < 1  scissors beat paper
    # 1 < 2  rock beats scissors
    # 2 < 0 paper beats rock

    for i in range(options_length):
        if(user_choice == options[i]):
            if((i == computer_choice_options_index)):
                break #game is still ongoing, user needs to type an input again
            elif(i == options_length - 1 and computer_choice_options_index == 0): # first option beats last option
                won("Computer")
            elif(i == 0 and computer_choice_options_index == options_length - 1):
                won("User")
            elif(i > computer_choice_options_index):
                won("User")
            else:
                won("Computer")

            break #the user choice was already found
