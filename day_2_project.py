# Tip Calculator

# Instructions
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

"""Code"""
print("I want to make your life easier. If you answer the questions below, "
      "I will tell you how much the bill per person is going to be")

bill = float(input("What was the total bill? EUR "))
tip = int(input("What percentage tip would you like to give? 12, 15 or 20? "))
people = int(input("With how many people do you want to split the bill? "))

total_bill = round(bill + (bill * (tip / 100)), 2)
bill_per_person = round(total_bill / people, 2)

print(f"The total bill: EUR {total_bill}. Divided by {people}, everyone has to pay: EUR {bill_per_person}")
