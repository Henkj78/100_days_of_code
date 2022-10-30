print("Welcome to Treasure Island.... This is going to be a lot of fun!\n")
print("Your mission is to find the hidden treasure")

cross_road = input('You are at a cross road. Where do you want to go? Enter "left" or "right" ').lower()
if cross_road == 'right':
    lake = input("You've come to a lake. There is an island in the middle of the lake. "
                 "Type 'wait' to wait for a boat. Type 'swim' to swim across.' ").lower()
    if lake == 'wait':
        door = input("You arrive at the island unharmed. There is a house with 3 doors. "
                     "One red, one yellow and one blue. Which colour do you choose? ")
        if door == 'blue':
            print("You found the treasure! You Win!")
        elif door == 'yellow':
            print("You walked into an empty room. Game over!")
        elif door == 'red':
            print("It's a room full of fire. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game over!")
    else:
        print("You've got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game over")



