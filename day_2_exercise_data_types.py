## Data Types

# Instructions

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# **Warning.** Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# Example Input

'''
39
'''

# Example Output

# 3 + 9 = 12

'''Code'''

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
num1 = two_digit_number[0]
num2 = two_digit_number[1]

total = int(num1) + int(num2)

print(num1 + ' + ' + num2 + ' = ' + str(total))