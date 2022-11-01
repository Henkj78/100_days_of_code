row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

print("Where do you want to put the treasure?")
position = input("Enter a two numbers between 1 and 4: ")

# convert to integers
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal - 1] = "X"

print(f"\n{row1}\n{row2}\n{row3}")