import random

# Exercise 2
#task 1:
# Create an empty list called display. for each letter in the chosen_word, add a "_" to display.

#task 2:
# Loop through each position in the chosen_word:
# if the letter at that position matches 'guess' then reveal that letter in the display at that position

word_list = ["ardvark", "baboo", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")

print(display)

chosen_letter = input("\nGuess a letter: ").lower()

for letter in chosen_letter:
    if letter in chosen_word:
        index_positions = chosen_word.index(letter)
        display[index_positions] = letter

print(display)
