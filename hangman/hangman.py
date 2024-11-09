import random

from hangman_module import random_words

choosen_word= random.choice(random_words)

display=[]

for letter in range(len(choosen_word)):
    display += "_"
lives=6
end_of_game = False

while not end_of_game:
    guessed_letter = input('guess a letter from the word : ').lower()
    if guessed_letter in display:
        print(f"you have already guessed the letter {guessed_letter} : ")

    for position in range(len(choosen_word)):
        position_letter = choosen_word[position]
        if position_letter == guessed_letter:
            display[position] = guessed_letter
    print(display)


    if guessed_letter not in choosen_word:
        lives -= 1
        print(f"the letter {guessed_letter} is not in the word")
        if lives == 0:
            end_of_game = True
            print("You lose")
    if "_" not in display:
        end_of_game = True
        print("You win!")
