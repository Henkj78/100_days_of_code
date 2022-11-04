#Password Generator Project

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!\n")

num_of_letters = int(input("How many letters would you like in your password? "))
num_of_numbers = int(input("How many numbers would you like in your password? "))
num_of_symbols = int(input("How many symbols would you like in your password? "))

# password = " "
#
# for letter in range(0, num_of_letters):
#     password += random.choice(letters)
#
# for number in range(0, num_of_numbers):
#     password += random.choice(numbers)
#
# for symbol in range(0, num_of_symbols):
#     password += random.choice(symbols)
#
#
# print(f"I think you should use this password:{password}")

password = []

for letter in range(0, num_of_letters):
    password.append(random.choice(letters))

for number in range(0, num_of_numbers):
    password.append(random.choice(numbers))

for symbol in range(0, num_of_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

password_shuffle = " "
for item in password:
    password_shuffle += item

print(f"I think you should use this password:{password_shuffle}")
