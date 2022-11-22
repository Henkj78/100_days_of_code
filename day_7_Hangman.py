import random
from day_7_hangman_word_list import word_list
from day_7_hangman_images import stages

chosen_word = random.choice(word_list)

print(f"Welcome to the Hangman game. Guess the {len(chosen_word)} letter word.")

# Player had 6 lives at the start of the game
lives = 6

display = []
for letter in chosen_word:
    display += "_"

end_of_game = False

while not end_of_game:
    chosen_letter = input("\nGuess a letter: ").lower()

    # check if user entered a letter they've already guessed
    if chosen_letter in display:
        print(f"You've already guessed the letter {chosen_letter}")

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == chosen_letter:
            display[i] = chosen_letter

    if chosen_letter not in chosen_word:
        print(f"You guessed {chosen_letter}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    # convert the list into a string
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
