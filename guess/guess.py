from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(PLAYER_NUMBER, RANDOM_NUMBER,turns):
    if (PLAYER_NUMBER > RANDOM_NUMBER):
        print("Too high")
        return turns -1
    elif (PLAYER_NUMBER < RANDOM_NUMBER):
        print("Too low.")
        return turns -1
    else:
        print(f"you got it the answer was {PLAYER_NUMBER}")
        return

def set_difficulty():
    GAME_LEVEL = input("Choose the difficulty level. Type easy or hard:").lower()
    if GAME_LEVEL == "easy":
        return EASY_LEVEL_TURNS
    elif GAME_LEVEL == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("you have entered the wrong difficulty level. please enter easy or hard")

RANDOM_NUMBER = randint(1,100)

def game():
    print("Welcome to the guess Game!")
    print("I am thinkning of a number between 1 to 100")

    turns = set_difficulty()

    PLAYER_NUMBER = 0
    while PLAYER_NUMBER != RANDOM_NUMBER:
        print(f"You have {turns} attemts remAining to guess the number")
        PLAYER_NUMBER = int(input("Make a guess :"))
        turns = check_answer(PLAYER_NUMBER,RANDOM_NUMBER,turns)

        if turns == 0:
            print("you lose the game becuase your turns are finished")
            return
        elif PLAYER_NUMBER != RANDOM_NUMBER:
            print("Guess again")

game()