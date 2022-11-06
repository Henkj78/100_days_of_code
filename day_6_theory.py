# print() is a function
# len() is a function

# What if we wanted to make our own functions?
# Start with the keyword def --> for defining the function
# Second is to give your function a name
# Direct after the name use ()
# Last use the : this says everything that comes after that line and is indented belongs with the function and it
# specify what the function should do

# Simple function:
def my_function():
    print("Hello")
    print("Bye")

# Now you created a function. If you run it, nothing will happen. Only when wy need it we can trigger it
# This means, "Calling or invoke" the function


# Call the function:
my_function()

"""Indentation"""
# All that what is indented belongs to the function --> scope of the function
# Be aware how you indent your code
# PEP: 4 spaces


def my_function2():
    print("The importance of indentation")
    block_inside = "yes"
    if block_inside == "yes":
        print("more spaces on if block")
    else:
        print("same spaces as if block")


my_function2()

"""While Loops"""
# A loop that will continue going while a particular condition is true
# Use it instead of a for loop if you don't know how many times the loop hase to run
something_is_true = 0

while something_is_true:
    print("do this")
    print("do this")
    print("and do this")

# Be aware of the infinite loop. Be shore that your loop stops at a particular moment

times = 0

while times < 6:
    print(f"The loop runs on {times}")
    # adds 1 every time the loop runs
    times += 1
print("The loop stopped because times is not < 6 anymore")

