import random

word_list = ["ardvark", "baboo", "camel"]

# chose a random word and assign it to chosen_word

chosen_word = random.choice(word_list)
print(chosen_word)

chosen_letter = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == chosen_letter:
        print(True)
    else:
        print(False)