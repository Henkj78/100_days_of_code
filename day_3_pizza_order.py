print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

bill = 0

if size == "s":
    bill += 15
elif size == "s":
    bill += 20
elif size == "l":
    bill += 25
else:
    print(f"Whe don't have size: {size}")

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: EUR {bill},-")



