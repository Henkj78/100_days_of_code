import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboo", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Player had 6 lives at the start of the game
lives = 6

display = []
for letter in chosen_word:
    display.append("_")

print(display)

end_of_game = False

while not end_of_game:
    chosen_letter = input("\nGuess a letter: ").lower()

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == chosen_letter:
            display[i] = chosen_letter

    if chosen_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
