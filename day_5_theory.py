"""Loops"""
# Thing that have to happen over and over again.

"""The For Loop"""
# Can be used easily with lists
# Can go through each item in a list and perform some action with each individual item

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(f"{fruit} Pie")
# prints once after the loop is done
print("Loop is done!")

# Range() Function
# can generate a range of numbers to loop through
total = 0
for number in range(1, 100, 2):  # Start: 1, Stop: up to 100 not including, Step: 2
    total += number
print(total)
